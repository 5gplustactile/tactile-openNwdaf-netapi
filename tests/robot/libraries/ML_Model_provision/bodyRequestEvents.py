def create_ml_model_subscription_body(notification_uri="http://127.0.0.1/notificationURI"):
    data = {
        "mLEventSubscs":[
            {
                "mLEvent":"SLICE_LOAD_LEVEL",
                "mLEventFilter": {
                    "anySlice": True
                }
            }
        ],
        "notifUri":notification_uri

    }
    return data

def create_bad_ml_model_subscription_body():
    data = {
        "mLEventSubscs":[
            {
                "mLEvent":"SLICE_LOAD_LEVEL",
                "mLEventFilter": {
                    "anySlice": True
                }
            }
        ]

    }
    return data
