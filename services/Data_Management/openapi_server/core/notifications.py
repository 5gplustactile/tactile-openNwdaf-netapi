from ..models.amf_event_notification import AmfEventNotification
from ..models.nsmf_event_exposure_notification import NsmfEventExposureNotification
from ..models.monitoring_report import MonitoringReport
from ..models.nef_event_exposure_notif import NefEventExposureNotif
from ..models.af_event_exposure_notif import AfEventExposureNotif
from ..models.notification_data import NotificationData
from ..models.sac_event_report import SACEventReport
from ..models.nnwdaf_data_management_subsc import NnwdafDataManagementSubsc
import random
from flask import current_app



def get_sub_data(sub:NnwdafDataManagementSubsc, atributo, corr_id):
    models = {
        'amf_data_sub': [AmfEventNotification, "notify_correlation_id"],
        'smf_data_sub': [NsmfEventExposureNotification, "notif_id"],
        'udm_data_sub': [MonitoringReport, "reference_id"],
        'af_data_sub': [AfEventExposureNotif, "notif_id"],
        'nef_data_sub': [NefEventExposureNotif, "notif_id"],
        'nrf_data_sub': [NotificationData, "nf_instance_uri"],
        'nsacf_data_sub': [SACEventReport, "notify_correlation_id"]
    }

    lista = models.get(atributo)
    model = lista[0]()
    setattr(model, lista[1], corr_id)
    return [model]

    

