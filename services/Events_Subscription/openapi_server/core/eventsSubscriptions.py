from ..core.responses import make_response, not_found_error, bad_request_error, internal_server_error
from ..models.nnwdaf_events_subscription import NnwdafEventsSubscription
from ..models.reporting_information import ReportingInformation
from ..util import dict_to_camel_case
from ..models.event_subscription import EventSubscription
from ..models.failure_event_info import FailureEventInfo
from ..core.controller_notifications import register_notification, remove_notification
from ..core.check_subscription import check_qos, check_nf_load, check_network_perf, check_user_data_congestion
from ..util import dict_to_camel_case
import secrets
from flask import current_app, Response
import os


def __check_id(id):
    current_app.logger.info(f"Checking id: {id}.")
    collection = current_app.config["db"].get_coll(os.getenv('EVENTS_SUBS_COL'))
    if collection.find_one({"id": id}) is None:
        current_app.logger.debug('Id not found')
        return True
    else:
        return False


def insert_sub(body:NnwdafEventsSubscription):
    collection = current_app.config["db"].get_coll(os.getenv('EVENTS_SUBS_COL'))
    
    subscription_id = secrets.token_hex(15)
    current_app.logger.debug("Checking Subscription")
    body_dict = body.to_dict()
    current_app.logger.debug(body_dict)
    if  body_dict["evt_req"] is None:
        body_dict["evt_req"]=ReportingInformation().to_dict()
    if body_dict["evt_req"]["notif_flag"] is None:
        body_dict["evt_req"]["notif_flag"]="ACTIVATE"

    reports= []
    for sub in body_dict["event_subscriptions"]:
        current_app.logger.debug(f"Checking sub with event: {sub['event']}")
        if sub["event"] == "QOS_SUSTAINABILITY":
            r = check_qos(body_dict, sub)
            if isinstance(r, Response):
                current_app.logger.debug(f"Error checking QoS event {r.json}")
                reports.append(FailureEventInfo(event=sub["event"], failure_code="UNAVAILABLE_DATA").to_dict())
            else:
                current_app.logger.debug(f"Registering in scheduler")
                sub["job_id"]=register_notification(body_dict, sub, subscription_id)
                current_app.logger.debug("Successfully logged QoS event")
        elif sub["event"] == "NF_LOAD":
            r = check_nf_load(body_dict, sub)

            if isinstance(r, Response):
                current_app.logger.debug(f"Error checking NF_LOAD event {r.json}")
                reports.append(FailureEventInfo(event=sub["event"], failure_code="UNAVAILABLE_DATA").to_dict())
            else:
                current_app.logger.debug(f"Registering in scheduler")
                sub["job_id"]=register_notification(body_dict, sub, subscription_id)
                current_app.logger.debug("Successfully logged NF_LOAD event")

        elif sub["event"] == "NETWORK_PERFORMANCE":
            r = check_network_perf(body_dict, sub)
            if isinstance(r, Response):
                current_app.logger.debug(f"Error checking NETWORK_PERFORMANCE event {r.json}")
                reports.append(FailureEventInfo(event=sub["event"], failure_code="UNAVAILABLE_DATA").to_dict())
            else:
                current_app.logger.debug(f"Registering in scheduler")
                sub["job_id"]=register_notification(body_dict, sub, subscription_id)
                current_app.logger.debug("Successfully logged NETWORK_PERFORMANCE event")
        
        elif sub["event"] == "USER_DATA_CONGESTION":
            r = check_user_data_congestion(body_dict, sub)
            if isinstance(r, Response):
                current_app.logger.debug(f"Error checking USER_DATA_CONGESTION event {r.json}")
                reports.append(FailureEventInfo(event=sub["event"], failure_code="UNAVAILABLE_DATA").to_dict())
            else:
                current_app.logger.debug(f"Registering in scheduler")
                sub["job_id"]=register_notification(body_dict, sub, subscription_id)
                current_app.logger.debug("Successfully logged USER_DATA_CONGESTION event")

        else:
            reports.append(FailureEventInfo(event=sub["event"], failure_code="UNAVAILABLE_DATA").to_dict())
    #We save the notification and eliminate the null
    if len(reports)>0:
        body_dict["fail_event_reports"] = reports

    if len(reports) != len(body_dict["event_subscriptions"]):
        current_app.logger.debug(f"Inserting subscription {subscription_id} in database")
        body_dict["id"] = subscription_id
        current_app.logger.debug(body_dict)
        collection.insert_one(body_dict)
        current_app.logger.debug(f"Subscription created!")
        #We return the response
        res = make_response(NnwdafEventsSubscription.from_dict(dict_to_camel_case(body_dict)), status=201)
        res.headers['Location'] = "/nnwdaf-eventssubscription/v1/subscriptions/"+str(body_dict["id"])
    else:
        current_app.logger.debug("Sub not created")
        res = internal_server_error(detail=f"Unable to obtain required data.", cause="UNAVAILABLE_DATA")
    return res


def delete_sub(id):
    collection = current_app.config["db"].get_coll(os.getenv('EVENTS_SUBS_COL'))

    #We verify that it exists. If it does not exist, a 404 is returned
    res = collection.find_one({"id": id})
    if not res:
        current_app.logger.debug("Id not found")
        return not_found_error(detail="Can't find a subscription with that id", cause="Id not found")
    
    for sub in res["event_subscriptions"]:
        current_app.logger.debug(f"Deleting job {sub["job_id"]}")
        remove_notification(sub["job_id"])
    
    #We eliminate subscription and notifications
    current_app.logger.debug(f"Deleting subscription {id}")
    collection.delete_one({"id": id})
    res = make_response("No Content", status=204)
    return res

def update_sub(id, body:NnwdafEventsSubscription):
    collection = current_app.config["db"].get_coll(os.getenv('EVENTS_SUBS_COL'))

    #We verify that it exists. If it does not exist, a 404 is returned
    res = collection.find_one({"id": id})
    if not res:
        current_app.logger.debug("Id not found")
        return not_found_error(detail="Can't find a subscription with that id", cause="Id not found")
    
    body_dict=body.to_dict()
    if  body_dict["evt_req"] is None:
        body_dict["evt_req"]=ReportingInformation().to_dict()
    if body_dict["evt_req"]["notif_flag"] is None:
        body_dict["evt_req"]["notif_flag"]="ACTIVATE"
    reports= []

    for sub in body_dict["event_subscriptions"]:
        current_app.logger.debug(sub)
        if sub["event"] == "QOS_SUSTAINABILITY":
            r = check_qos(body_dict, sub)
            if isinstance(r, Response):
                current_app.logger.debug(r.json)
                reports.append(FailureEventInfo(event=sub["event"], failure_code="UNAVAILABLE_DATA").to_dict())
        elif sub["event"] == "NF_LOAD":
            r = check_nf_load(body_dict, sub)
            if isinstance(r, Response):
                reports.append(FailureEventInfo(event=sub["event"], failure_code="UNAVAILABLE_DATA").to_dict())
        elif sub["event"] == "NETWORK_PERFORMANCE":
            r = check_network_perf(body_dict, sub)
            if isinstance(r, Response):
                reports.append(FailureEventInfo(event=sub["event"], failure_code="UNAVAILABLE_DATA").to_dict())
        elif sub["event"] == "USER_DATA_CONGESTION":
            r = check_user_data_congestion(body_dict, sub)
            if isinstance(r, Response):
                reports.append(FailureEventInfo(event=sub["event"], failure_code="UNAVAILABLE_DATA").to_dict())
        else:
            reports.append(FailureEventInfo(event=sub["event"], failure_code="UNAVAILABLE_DATA").to_dict())

    for sub in res["event_subscriptions"]:
        current_app.logger.debug(f"Deleting job {sub["job_id"]}")
        remove_notification(sub["job_id"])

    if len(reports) != len(body.event_subscriptions):
        for sub in body_dict["event_subscriptions"]:
            if sub["event"] == "QOS_SUSTAINABILITY":
                r = check_qos(body_dict, sub)
                if not isinstance(r, FailureEventInfo):
                        sub["job_id"] = register_notification(body_dict, sub, id)
            if sub["event"] == "NF_LOAD":
                r = check_nf_load(body_dict, sub)
                if not isinstance(r, FailureEventInfo):
                        sub["job_id"] = register_notification(body_dict, sub, id)
            if sub["event"] == "NETWORK_PERFORMANCE":
                r = check_network_perf(body_dict, sub)
                if not isinstance(r, FailureEventInfo):
                        sub["job_id"] = register_notification(body_dict, sub, id)
            if sub["event"] == "USER_DATA_CONGESTION":
                r = check_user_data_congestion(body_dict, sub)
                if not isinstance(r, FailureEventInfo):
                        sub["job_id"] = register_notification(body_dict, sub, id)


        body_dict={
            key: value for key, value in body_dict.items() if value is not None
        }
        collection.update_one({"id": id}, {"$set":body_dict}, upsert=False)

        r = collection.find_one({"id": id})

        res = make_response(NnwdafEventsSubscription.from_dict(dict_to_camel_case(r)), status=200)
    else:
        res = make_response(body, status=400)
        
        return res