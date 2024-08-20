from ..db.db import MongoDatabase
from ..core.responses import make_response, not_found_error, bad_request_error
from ..core.controller_notifications import controller_notifications
from flask import current_app
import secrets
import os

class mlSubs_controller:

    notify = controller_notifications()

    def __check_id(self, id):
        current_app.logger.info("Checking id.")
        collection = current_app.config["db"].get_coll(os.getenv('ML_PROVISION_SUBS_COL'))
        if collection.find_one({"id": id}) is None:
            return True
        else:
            return False

    def insert_mlsub(self, body):
        collection = current_app.config["db"].get_coll(os.getenv('ML_PROVISION_SUBS_COL'))
        # find = collection.find_one({"notif_uri": body.notif_uri})
        # if find is not None:
        #     current_app.logger.error("notification_uri in database.")
        #     return bad_request_error(detail="Enter a notification_uri that is not already stored", cause="notification_uri exist", invalid_params="notification_uri")
        
        b = body.to_dict()
        b["id"] = secrets.token_hex(15)
        result = collection.insert_one(b)

        # res = self.notify.register_notification(body, b["id"])
        res = make_response(body, status=201)
        res.headers['Location'] = "/nnwdaf-mlmodelprovision/v1/subscriptions/"+str(b["id"])
        return res

    def delete_mlsub(self, id):
        collection = current_app.config["db"].get_coll(os.getenv('ML_PROVISION_SUBS_COL'))
        res = self.__check_id(id)
        if res is True:
            return not_found_error(detail="Can't find a subscription with that id", cause="Id not found")
        result=collection.delete_one({"id": id})
        # self.notify.remove_notification(id)
        res = make_response("No Content", status=204)
        return res
    
    def update_mlsub(self, id, body):
        collection = current_app.config["db"].get_coll(os.getenv('ML_PROVISION_SUBS_COL'))
        res = self.__check_id(id)
        if res is True:
            return not_found_error(detail="Can't find a subscription with that id", cause="Id not found")
        body_upd=body.to_dict()
        body_upd={
            key: value for key, value in body_upd.items() if value is not None
        }
        result = collection.update_one({"id": id}, {"$set":body_upd}, upsert=False)

        # self.notify.remove_notification(id)
        # self.notify.register_notification(body, id)
        res = make_response(body, status=200)

        r = collection.find_one({"id": id},{"_id": 0})
        res = make_response(r, status=200)
        return res