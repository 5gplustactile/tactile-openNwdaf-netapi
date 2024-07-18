def create_event_data_subscription_body(notification_uri="http://127.0.0.1/notificationURI"):
    data = {
        "notifCorrId":"notif",
        "notificURI":notification_uri,
        "anaSub":{
            "eventSubscriptions":[
                {
                    "event":"SLICE_LOAD_LEVEL"
                }
            ]
        }
    }
    return data

def create_bad_event_data_subscription_body(notification_uri="http://127.0.0.1/notificationURI"):
    data = {
        "notificURI":notification_uri,
        "anaSub":{
            "eventSubscriptions":[
                {
                    "event":"SLICE_LOAD_LEVEL"
                }
            ]
        }
    }
    return data
