from ..models.nnwdaf_data_management_subsc import NnwdafDataManagementSubsc
from ..models.nnwdaf_data_management_notif import NnwdafDataManagementNotif
from ..models.data_notification import DataNotification
from ..core.notifications import get_sub_data
from ..core.responses import bad_request_error, make_response
from flask_apscheduler import APScheduler
from datetime import datetime
from flask import current_app
import secrets
import requests

class controller_notifications():

    scheduler = ""
    users = {}
    
    def __data_sub_periodic_notification__(self, body:NnwdafDataManagementSubsc, sub_id):
        atributos = [('amf_data_sub','amf_event_notifs'),
                    ('smf_data_sub', 'smf_event_notifs'),
                    ('udm_data_sub', 'udm_event_notifs'),
                    ('af_data_sub','af_event_notifs'),
                    ('nef_data_sub','nef_event_notifs'),
                    ('nrf_data_sub', 'nrf_event_notifs'),
                    ('nsacf_data_sub', 'nsacf_event_notifs')]
        # Utilizar un bucle if para verificar si cada atributo existe
        data_notification=DataNotification()
        for atributo_sub, atributo_notif in atributos:
            if hasattr(body.data_sub, atributo_sub) and getattr(body.data_sub, atributo_sub) is not None:
                notif = get_sub_data(getattr(body.data_sub, atributo_sub), atributo_sub, body.notif_corr_id)
                setattr(data_notification, atributo_notif, notif)
        data_notification.time_stamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+"Z"
        notification = NnwdafDataManagementNotif(data_notification=data_notification,
                                                   notif_corr_id=body.notif_corr_id,
                                                   notif_timestamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+"Z")

        try:
            response = requests.post(body.notific_uri, json=notification.to_dict(), timeout=5)
        except requests.exceptions.RequestException as e:
            print(f"Error al enviar notificación a {body.notific_uri}: {str(e)}")

    def register_notification(self, body:NnwdafDataManagementSubsc, sub_id):
        self.scheduler = current_app.config["scheduler"]
        self.users[sub_id]=[]
        current_app.logger.debug(body)
        if body.ana_sub is not None:
            current_app.logger.debug("ana_sub side")
        if body.data_sub is not None:
            current_app.logger.debug("data_sub side")
            job_id = secrets.token_hex(16)
            self.users[sub_id].append(job_id)
            ####################################
            # SUBSCRIPCION A LOS NF
            ####################################
            current_app.config["scheduler"].add_job(func=self.__data_sub_periodic_notification__,
                                                                     args=(body, sub_id),
                                                                     trigger="interval",
                                                                     seconds=10,
                                                                     max_instances=1, 
                                                                     id=job_id)

        
        return make_response(body, status=201)


    def remove_notification(self, id):
        for job_id in self.users[id]:
            current_app.config["scheduler"].remove_job(job_id)
        del self.users[id]
        current_app.logger.debug("Periodic notification removed.")
    

