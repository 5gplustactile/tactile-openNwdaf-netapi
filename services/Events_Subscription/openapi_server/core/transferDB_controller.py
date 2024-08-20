from ..core.responses import make_response, not_found_error
from  flask import current_app
import secrets
import os

class transferDB_controller:

    def __check_id(self, id):
        current_app.logger.info("Checking id.")
        collection = current_app.config["db"].get_coll(os.getenv('TRANSFER_SUBS_COL'))
        if collection.find_one({"id": id}) is None:
            current_app.logger.debug('True')
            return True
        else:
            return False

    def insert_transfer(self, body):

        current_app.logger.debug("Start insert.")

        collection = current_app.config["db"].get_coll(os.getenv('TRANSFER_SUBS_COL'))
        if body._subs_trans_infos[0]._trans_req_type=="PREPARE":

            current_app.logger.info("Creating id.")
            b = body.to_dict()
            b["id"] = secrets.token_hex(15)
            current_app.logger.debug("Subscription created.")
            result = collection.insert_one(b)

            r = collection.find_one({"id": b["id"]})

            res = make_response(r['subs_trans_infos'], status=201)
            res.headers['Location'] = "/nnwdaf-eventssubscription/v1/transfers/"+str(b["id"])
            return res
        elif body._subs_trans_infos[0]._trans_req_type=="TRANSFER":
            res = make_response("No Content", status=204)
            return res

    def delete_transfer(self, id):
        collection = current_app.config["db"].get_coll(os.getenv('TRANSFER_SUBS_COL'))
        res = self.__check_id(id)
        if res is True:
            return not_found_error(detail="Can't find a subscription with that id", cause="Id not found")
        result=collection.delete_one({"id": id})
        res = make_response("No Content", status=204)
        return res
    
    def update_transfer(self, id, body):
        collection = current_app.config["db"].get_coll(os.getenv('TRANSFER_SUBS_COL'))
        if body._subs_trans_infos[0]._trans_req_type == "PREPARE":
            res = self.__check_id(id)
            if res is True:
                return not_found_error(detail="Can't find a subscription with that id", cause="Id not found")
            body_upd=body.to_dict()
            body_upd={
                key: value for key, value in body_upd.items() if value is not None
            }
            result = collection.update_one({"id": id}, {"$set":body_upd}, upsert=False)
            res = make_response(body, status=200)
            return res
        elif body._subs_trans_infos[0]._trans_req_type == "TRANSFER":
            res = self.delete_transfer(id)
            return res
