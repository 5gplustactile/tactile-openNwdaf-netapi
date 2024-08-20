from ..models.nwdaf_ml_model_prov_subsc import NwdafMLModelProvSubsc
from ..models.nwdaf_ml_model_prov_notif import NwdafMLModelProvNotif
from ..core.notifications import make_notification
from ..core.responses import bad_request_error, make_response
from flask_apscheduler import APScheduler
from flask import current_app
import secrets
import requests

class controller_notifications():

    scheduler = ""
    users = {}

    notification = NwdafMLModelProvNotif()
    
    def __evt_req_periodic_notification__(self, body:NwdafMLModelProvSubsc, sub_id):
        events = []
        for sub in body.m_l_event_subscs:
            try:
                events.append(make_notification(body, sub, sub_id))
            except KeyError:
                print("Evento no disponible")

        try:
            self.notification.subscription_id = sub_id
            self.notification.event_notifs=events
            response = requests.post(body.notif_uri, json=self.notification.to_dict(), timeout=5)
        except requests.exceptions.RequestException as e:
            print(f"Error al enviar notificación a http://localhost:8099: {str(e)}")


    def register_notification(self, body:NwdafMLModelProvSubsc, sub_id):
        self.scheduler = current_app.config["scheduler"]
        self.users[sub_id]=[]
        current_app.logger.debug(body.event_req)


        if body.event_req is not None and body.event_req.notif_method is not None and body.event_req.rep_period is not None:     
            current_app.logger.debug("EVT_REQ")
            job_id = secrets.token_hex(16)
            self.users[sub_id].append(job_id)
            if body.event_req.notif_method == "PERIODIC":
                current_app.config["scheduler"].add_job(func=self.__evt_req_periodic_notification__,
                                                                    args=(body, sub_id),
                                                                    trigger="interval",
                                                                    seconds=body.event_req.rep_period,
                                                                    max_instances=1, 
                                                                    id=job_id)
                current_app.logger.debug(f"Periodic notification created. It will be sent to  {body.notif_uri} every {body.event_req.rep_period} seconds.")
            return make_response(body, status=201)
        else:
            return bad_request_error("Invalid event requirements", "", "event_req")

    def remove_notification(self, id):
        for job_id in self.users[id]:
            current_app.config["scheduler"].remove_job(job_id)
        del self.users[id]
        current_app.logger.debug("Periodic notification removed.")
    

