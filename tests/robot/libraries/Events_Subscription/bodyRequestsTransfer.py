def create_transfer_event_subscription(event="SLICE_LOAD_LEVEL", transReqType="PREPARE"):
    data = {
                "subsTransInfos":[
                    {
                        "transReqType": transReqType,
                        "nwdafEvSub":{
                            "eventSubscriptions":[
                                {
                                    "event": event
                                }
                            ]
                        },
                        "consumerId": "NF1"
                    }
                ]
            }
    return data


def create_bad_transfer_event_subscription(event="SLICE_LOAD_LEVEL"):
    data = {
                "subsTransInfos":[
                    {
                        "nwdafEvSub":{
                            "eventSubscriptions":[
                                {
                                    "event": event
                                }
                            ]
                        },
                        "consumerId": "NF1"
                    }
                ]
            }
    return data