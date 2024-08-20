def create_event_subscription_body(notification_uri="http://127.0.0.1/notificationURI"):
    data = {
        "notificationURI": notification_uri,
        "eventSubscriptions":[
            {
                "event": "SLICE_LOAD_LEVEL",
                "anySlice": True,
                "notification Method":"PERIODIC"
            }
        ],
        "evtReq":{
            "notifMethod": "ON_EVENT_DETECTION"
        }
    }
    return data

def create_bad_event_subscription_body(notification_uri="http://127.0.0.1/notificationURI"):
    data = {
        "notificationURI": notification_uri,
        "evtReq":{
            "notifMethod": "ON_EVENT_DETECTION"
        }
    }
    return data

def nokia_event_subscription_body():
    data = {
            "eventSubscriptions": [
            {
            "event": "UE_MOBILITY", "extraReportReq": {
            "accuracy": "HIGH",
            "startTs": "2022-05- 31T06:15:00.000Z",
            "endTs": "2022-05- 31T07:30:00.000Z", "sampRatio": 5
            },
            "notificationMethod": "PERIODIC",
            "tgtUe": { "anyUe": null, "supis": ["2"],"intGroupIds": null }
            } ],
            "evtReq": {
            "notifMethod": "PERIODIC", "monDur": "2022-05-31T07:30:00.000Z", "repPeriod": 15
            },
            "notificationURI": "https://fe8kcr6hnn7f3iuc.b.reque stbin.net"
    }
    return data
