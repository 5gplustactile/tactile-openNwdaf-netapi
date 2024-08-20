from ..models.nnwdaf_events_subscription import NnwdafEventsSubscription
from ..models.event_subscription import EventSubscription
from ..models.nnwdaf_events_subscription_notification import NnwdafEventsSubscriptionNotification
from ..models.failure_event_info import FailureEventInfo
from ..db.db import MongoDatabase
from ..util import dict_to_camel_case, clean_empty
from ..core.check_subscription import check_qos
from ..core.notifications import notification
import json
import os
from ..encoder import JSONEncoder
from flask import current_app
import secrets
import requests

notifications = notification()
client = MongoDatabase()

def __periodic_notifications__(body:dict, sub:dict, subscription_id):
    if body["evt_req"]["notif_flag"] == "ACTIVATE" or body["evt_req"]["notif_flag"] == "RETRIEVAL":
        #We use the function for the indicated event and save the response
        funcion = sub["event"].lower()+"_periodic_notification"
        if hasattr(notifications, funcion) and callable(getattr(notifications, funcion)):
            notification = NnwdafEventsSubscriptionNotification()
            notification.event_notifications = [clean_empty(getattr(notifications, funcion)(
                NnwdafEventsSubscription.from_dict(dict_to_camel_case(body)),
                EventSubscription.from_dict(dict_to_camel_case(sub))))]
            
            notification.subscription_id = subscription_id
            notification.notif_corr_id=body["notif_corr_id"]

            try:
                #We send the notification
                headers = {
                    'Content-Type': 'application/json'
                }
                response = requests.post(body["notification_uri"], headers=headers, data=json.dumps(notification, cls=JSONEncoder), timeout=5)

                if response.status_code == 204:
                    print(f"Notification sent! to {body["notification_uri"]}")
                else:
                    body["evt_req"]["notif_flag"] = "DEACTIVATE"
                    body_upd={
                        key: value for key, value in body.items() if value is not None
                    }
                    # client.get_coll(os.getenv('EVENTS_SUBS_COL')).update_one({"id": subscription_id}, {"$set":body_upd}, upsert=False)

                    
            except requests.exceptions.RequestException as e:
                body["evt_req"]["notif_flag"] = "DEACTIVATE"
                body={
                    key: value for key, value in body.items() if value is not None
                }
                # client.get_coll(os.getenv('EVENTS_SUBS_COL')).update_one({"id": subscription_id}, {"$set":body}, upsert=False)



def __threshold_notifications__(body:dict, sub:dict, subscription_id):
    try:
        if body["evt_req"]["notif_flag"] == "ACTIVATE" or body["evt_req"]["notif_flag"] == "RETRIEVAL":
            #We use the function for the indicated event and save the response
            funcion = sub["event"].lower()+"_periodic_notification"
            if hasattr(notifications, funcion) and callable(getattr(notifications, funcion)):
                notification = NnwdafEventsSubscriptionNotification()
                notification.event_notifications = [getattr(notifications, funcion)(
                    NnwdafEventsSubscription.from_dict(dict_to_camel_case(body)),
                    EventSubscription.from_dict(dict_to_camel_case(sub)))]
                
                notification.subscription_id = subscription_id
                notification.notif_corr_id=body["notif_corr_id"]

                try:
                    #We send the notification
                    headers = {
                        'Content-Type': 'application/json'
                    }
                    response = requests.post(body["notification_uri"], headers=headers, data=json.dumps(notification, cls=JSONEncoder), timeout=5)

                    if response.status_code == 204:
                        print(f"Notification sent! to {body["notification_uri"]}")
                    else:
                        body["evt_req"]["notif_flag"] = "DEACTIVATE"
                        body_upd={
                            key: value for key, value in body.items() if value is not None
                        }
                        client.get_coll(os.getenv('EVENTS_SUBS_COL')).update_one({"id": subscription_id}, {"$set":body_upd}, upsert=False)

                        
                except requests.exceptions.RequestException as e:
                    body["evt_req"]["notif_flag"] = "DEACTIVATE"
                    body={
                        key: value for key, value in body.items() if value is not None
                    }
                    client.get_coll(os.getenv('EVENTS_SUBS_COL')).update_one({"id": subscription_id}, {"$set":body}, upsert=False)

            else:
                raise Exception

    except KeyError:
        print("Event unavailable")

def register_notification(body, sub, subscription_id):

    if body["evt_req"]["notif_method"] is not None and body["evt_req"]["rep_period"] is not None:
        period = body["evt_req"]["rep_period"]
        notif_method = body["evt_req"]["notif_method"]
    else:
        period = sub["repetition_period"]
        notif_method = sub["notification_method"]
    
    job_id = secrets.token_hex(15)
    if notif_method == "PERIODIC":
        current_app.config["scheduler"].add_job(func=__periodic_notifications__,
                                    args=(body, sub, subscription_id),
                                    trigger="interval",
                                    seconds=period,
                                    max_instances=1, 
                                    id=job_id)
    # elif notif_method in ["THRESHOLD", "ON_EVENT_DETECTION", None]:
    #     current_app.config["scheduler"].add_job(func=__threshold_notifications__,
    #                                 args=(body, sub, subscription_id),
    #                                 trigger="interval",
    #                                 seconds=60,
    #                                 max_instances=1, 
    #                                 id=job_id)
    return job_id

def remove_notification(job_id):
    current_app.config["scheduler"].remove_job(job_id)
    current_app.logger.debug(f"Job with id {job_id} removed.")



