from ..models.nwdaf_ml_model_prov_notif import NwdafMLModelProvNotif
from ..models.ml_event_subscription import MLEventSubscription
from ..models.ml_event_notif import MLEventNotif
import random
from flask import current_app

def make_notification(body, sub:MLEventSubscription, sub_id):
    event_notify = MLEventNotif(event=sub.m_l_event,
                                notif_corre_id=sub_id,
                                m_l_file_addr="address (e.g. a URL or an FQDN) of the ML model file",
                                validity_period=None)
    
    return event_notify