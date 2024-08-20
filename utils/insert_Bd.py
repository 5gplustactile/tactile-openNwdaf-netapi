import random
from datetime import datetime, timedelta
from pymongo import MongoClient

#events=["NSI_LOAD_LEVEL"]
tss = []
accuracys = ["LOW", "MEDIUM", "HIGH", "Highest"]
nfInstanceIds = ["c5262086-670d-4a4c-bc65-f32c25da1514", "c5262086-670d-4a4c-bc65-f32c25da1515"]
setIds = ['setxyz.nrfset.5gc.mnc456.mcc123', 'setxyz.nrfset.5gc.mnc123.mcc456']
snssaiss = [{"sst":100,"sd":"abcdef"}, {"sst":101,"sd":"abcdef"}, {"sst":102,"sd":"abcdef"}, {"sst":103,"sd":"abcdef"}]
nftypes =["NRF", "AMF", "UPF"]
networkAreas = [{"ecgis":[{"plmn_id":{"mcc":"456", "mnc":"123"},"eutra_cell_id":"abc1234", "nid": "abcde123456"}]},
                 {"g_ran_node_ids":[{"plmnId":{"mcc":"456", "mnc":"123"},"n3IwfId":"1A2B3C", "gNbId":{"bitLength":25, "gNBValue":"abc123"}, "ngeNbId": "MacroNGeNB-123ab", "wagfId": "1A2B3C", "tngfId":"1A2B3C", "nid":"abcde123456", "eNbId": "MacroeNB-123ab"}]},
                 {"ncgis":[{"plmnId":{"mcc":"456", "mnc":"123"}, "nrCellId": "abcde1234", "nid": "abcde123456"}]},
                 {"tais":[{"plmnId":{"mcc":"456", "mnc":"123"}, "tac": "ab12", "nid": "abcde123456"}]}
                ]
locs = [{"eutraLocation":{'tai':{"plmnId":{"mcc":"456", "mnc":"123"}, "tac": "ab12", "nid": "abcde123456"}, 'ecgi': {"plmnId":{"mcc":"456", "mnc":"123"},"eutraCellId":"abc1234", "nid": "abcde123456"}, 'ageOfLocationInformation': 1, 'ueLocationTimestamp':'2023-07-13T08:45:18Z', 'geographicalInformation': 'AAAAAAAAAAAAAAAA', 'geodeticInformation': 'BBBBBBBBBBBBBBBBBBBB', 'globalNgenbId': {"plmnId":{"mcc":"456", "mnc":"123"},"n3IwfId":"1A2B3C", "gNbId":{"bitLength":25, "gNBValue":"abc123"}, "ngeNbId": "MacroNGeNB-123ab", "wagfId": "1A2B3C", "tngfId":"1A2B3C", "nid":"abcde123456", "eNbId": "MacroeNB-123ab"}}},
        {"nrLocation":{'tai':{"plmnId":{"mcc":"456", "mnc":"123"}, "tac": "ab12", "nid": "abcde123456"}, "ncgi": {"plmnId":{"mcc":"456", "mnc":"123"}, "nrCellId": "abcde1234", "nid": "abcde123456"}, "globalGnbId":  {"plmnId":{"mcc":"456", "mnc":"123"},"n3IwfId":"1A2B3C", "gNbId":{"bitLength":25, "gNBValue":"abc123"}, "ngeNbId": "MacroNGeNB-123ab", "wagfId": "1A2B3C", "tngfId":"1A2B3C", "nid":"abcde123456", "eNbId": "MacroeNB-123ab"}}}
        ]
nw_perf_types=["GNB_ACTIVE_RATIO", "GNB_COMPUTING_USAGE", "GNB_MEMORY_USAGE"]
devicesSpeeds=[
    {'h_speed': 40, 'bearing': 50},
    {'h_speed': 50, 'bearing': 60, 'h_uncertainty':70},
    {'h_speed': 60, 'bearing': 70, 'v_speed': 80, 'v_direction':"UPWARD"},
    {'h_speed': 70, 'bearing': 80, 'v_speed': 90, 'v_direction':"DOWNWARD", 'h_uncertainty': 100, 'v_uncertainty': 110}
    
]
deviceTypes=[
    "MOBILE_PHONE", "SMART_PHONE", "TABLET"
]

uri = "mongodb://root:example@0.0.0.0:27018"
client = MongoClient(uri)
db = client["nwdaf"]
col = db["analytics"]

col.drop()
col = db["analytics"]

for i in range (10):
    start_date = datetime(2023, 6, 1)
    end_date = datetime(2023, 6, 30)

    # Calcular la diferencia de tiempo entre las fechas de inicio y fin
    time_delta = end_date - start_date

    # Generar una fecha aleatoria dentro del rango
    random_date = start_date + timedelta(seconds=random.randint(0, time_delta.total_seconds()))

    # Formatear la fecha en el formato deseado
    tss.append(random_date)

jsons=[]
#
nf_load_aleatorio = {
    "owner": "entityA",
    "gdpr_analytics": True,
    "createdAt":"2023-07-21T11:39:27.755Z",
    "updatedAt":"2023-07-21T11:39:27.755Z",
    "eventType": "NF_LOAD",
    'data':{
        'ts': datetime(2023, 6, 2),
        'supi': "4561230000000000",
        'networkArea':{"ecgis":[{"plmn_id":{"mcc":"456", "mnc":"123"},"eutra_cell_id":"abc1234", "nid": "abcde123456"}]},
        'nfType': "UPF",
        'nfInstanceId': "c5262086-670d-4a4c-bc65-f32c25da1514",
        'nfSetId': 'setxyz.nrfset.5gc.mnc456.mcc123',
        "nfStatus":{
            "statusRegistered": 1,
            "statusUnregistered": 2,
            "statusUndiscoverable": 3
        },
        "nfCpuUsage": 1,
        "nfMemoryUsage": 1,
        "nfStorageUsage": 20,
        "nfLoadLevelAverage": 30,
        "nfLoadlevelPeak": 20,
        "nfLoadAvgInAoi": 10,
        'snssai': {"sst":100,"sd":"abcdef"}
    }
    
}
jsons.append(nf_load_aleatorio)
col.insert_one(nf_load_aleatorio)

nw_perf_aleatorio = {
    "owner": "entityA",
    "gdpr_analytics": True,
    "createdAt":"2023-07-21T11:39:27.755Z",
    "updatedAt":"2023-07-21T11:39:27.755Z",
    "eventType":"NETWORK_PERFORMANCE",
    'data':{
        'ts': datetime(2023, 6, 3),
        'intGroupId': "id300",
        'supi': "4561230000000000",
        'networkArea':{"ncgis":[{"plmnId":{"mcc":"456", "mnc":"123"}, "nrCellId": "abcde1234", "nid": "abcde123456"}]},
        'nwPerfType': "GNB_ACTIVE_RATIO",
        'anaPeriod':{
            'startTime':datetime(2023, 6, 1),
            'stopTime': datetime(2023, 6, 2)
        },
        'relativeRatio':20,
        'absoluteNum': 5
    }
}
jsons.append(nw_perf_aleatorio)
col.insert_one(nw_perf_aleatorio)

qos_requ_aleatorio = {
    "owner": "entityA",
    "gdpr_analytics": True,
    "createdAt":"2023-07-21T11:39:27.755Z",
    "updatedAt":"2023-07-21T11:39:27.755Z",
    'eventType':"QOS_SUSTAINABILITY",
    'data':{
        'ts': datetime(2023, 6, 4),
        'areaInfo':{"tais":[{"plmn_id":{"mcc":"456", "mnc":"123"}, "tac": "ab12", "nid": "abcde123456"}]},
        'startTs': '2023-07-13T08:45:18Z',
        'endTs': '2023-07-13T08:45:18Z',
        'qosFlowRetThd':{
            'relTimeUnit': "HOUR",
            'relFlowRatio': 20
        },
        'ranUeThrouThd': "200.0 bps",
        'snssai': {"sst":101,"sd":"abcdef"},
        "_5qi": 2
    }
}
jsons.append(qos_requ_aleatorio)
col.insert_one(qos_requ_aleatorio)

qos_requ_aleatorio2 = {
    "owner": "entityA",
    "gdpr_analytics": True,
    "createdAt":"2023-07-21T11:39:27.755Z",
    "updatedAt":"2023-07-21T11:39:27.755Z",
    'eventType':"QOS_SUSTAINABILITY",
    'data':{
        'ts': datetime(2023, 6, 5),
        'areaInfo':{"tais":[{"plmn_id":{"mcc":"456", "mnc":"123"}, "tac": "ab12", "nid": "abcde123456"}]},
        'startTs': '2023-07-13T08:45:18Z',
        'endTs': '2023-07-13T08:45:18Z',
        'qosFlowRetThd':{
            'relFlowNum': 30,
            'relTimeUnit': "MINUTE",
        },
        'ranUeThrouThd': "100.0 bps",
        'snssai': {"sst":102,"sd":"abcdef"},
        'gfbr_ul': "10.0 bps",
        'gfbr_dl': "10.0 bps",
        'res_type': "NON_GBR",
        'pdb': 100,
        'per': '1E-1',
        'deviceSpeed': {'h_speed': 40, 'bearing': 50},
        'deviceType': "MOBILE_PHONE"
    }
}

jsons.append(qos_requ_aleatorio2)
col.insert_one(qos_requ_aleatorio2)

#Randoms
for i in range (10):
    ts = random.choice(tss)
    accuracy = random.choice(accuracys)
    nfInstanceId = random.choice(nfInstanceIds)
    setId = random.choice(setIds)
    snssai = random.choice(snssaiss)
    anyUe = random.choice([True, False])
    nfType = random.choice(nftypes)
    sliceLoadLevelInfos=random.randint(1, 20)


    # slice_load_aleatorio = {
    #     "owner": "entityA",
    #     "gdpr_analytics": True,
    #     "createdAt":"2023-07-21T11:39:27.755Z",
    #     "updatedAt":"2023-07-21T11:39:27.755Z",
    #     "eventType": "LOAD_LEVEL_INFORMATION",
    #     "data":{
    #         'ts': ts,
    #         "snssais": random.sample(snssaiss, 2),
    #         "loadLevelInformation": random.randint(0, 30)
    #         }
            
    # }

    # jsons.append(slice_load_aleatorio)
    # col.insert_one(slice_load_aleatorio)

    # nsi_aleatorio = {
    #     "owner": "entityA",
    #     "gdpr_analytics": True,
    #     "createdAt":"2023-07-21T11:39:27.755Z",
    #     "updatedAt":"2023-07-21T11:39:27.755Z",
    #     "eventType": "NSI_LOAD_LEVEL",
    #     'data':{
    #         'ts': ts,
    #         "nsiId": "SliceID",
    #         'snssai': random.choice(snssaiss),
    #         "resUsage":{
    #             "cpuUsage":random.randint(0, 30),
    #             "memoryUsage":random.randint(0, 30),
    #             "storageUsage":random.randint(0, 30)
    #         },
    #         "numOfExceedLoadLevelThr": random.randint(0, 30),
    #         "exceedLoadLevelThrInd": random.choice(["true", "false"]),
    #         "networkArea":random.choice(networkAreas),
    #         "timePeriod":{
    #             "startTime": '2023-07-13T08:45:18Z',
    #             "stopTime": '2023-07-17T12:35:38Z'
    #         },
    #         "resUsgThrCrossTimePeriod":[{
    #             "startTime": '2023-07-13T08:45:18Z',
    #             "stopTime": '2023-07-17T12:35:38Z'
    #         }],
    #         "numOfUes":{
    #             "number": random.uniform(0.0, 30.0),
    #             "variance": random.uniform(0.0, 30.0),
    #             "skewness": random.uniform(0.0, 30.0)
    #         },
    #         "numOfPduSess":{
    #             "number": random.uniform(0.0, 30.0),
    #             "variance": random.uniform(0.0, 30.0),
    #             "skewness": random.uniform(0.0, 30.0)
    #         }
    #     }
    # }

    # jsons.append(nsi_aleatorio)
    # col.insert_one(nsi_aleatorio)

    nf_load_aleatorio = {
        "owner": "entityA",
        "gdpr_analytics": True,
        "createdAt":"2023-07-21T11:39:27.755Z",
        "updatedAt":"2023-07-21T11:39:27.755Z",
        "eventType": "NF_LOAD",
        'data':{
            'ts': ts,
            'supi': "4561230000000000",
            'networkArea':random.choice(networkAreas),
            'nfType': nfType,
            'nfInstanceId': nfInstanceId,
            'nfSetId': setId,
            "nfStatus":{
                "statusRegistered": random.randint(1, 100),
                "statusUnregistered": random.randint(1,100 ),
                "statusUndiscoverable": random.randint(1, 100)
            },
            "nfCpuUsage": 1,
            "nfMemoryUsage": 1,
            "nfStorageUsage": 20,
            "nfLoadLevelAverage": 30,
            "nfLoadlevelPeak": 20,
            "nfLoadAvgInAoi": 10,
            'snssai': random.choice(snssaiss)
        }
        
    }

    jsons.append(nf_load_aleatorio)
    col.insert_one(nf_load_aleatorio)

    nw_perf_aleatorio = {
        "owner": "entityA",
        "gdpr_analytics": True,
        "createdAt":"2023-07-21T11:39:27.755Z",
        "updatedAt":"2023-07-21T11:39:27.755Z",
        "eventType":"NETWORK_PERFORMANCE",
        'data':{
            'ts': ts,
            'intGroupId': "id300",
            'supi': "4561230000000000",
            'networkArea':random.choice(networkAreas),
            'nwPerfType': random.choice(nw_perf_types),
            'anaPeriod':{
                'startTime':ts,
                'stopTime': ts
            },
            'relativeRatio':random.randint(1, 100),
            'absoluteNum': random.randint(1, 20)
        }
    }
    jsons.append(nw_perf_aleatorio)
    col.insert_one(nw_perf_aleatorio)

    qos_requ_aleatorio = {
        "owner": "entityA",
        "gdpr_analytics": True,
        "createdAt":"2023-07-21T11:39:27.755Z",
        "updatedAt":"2023-07-21T11:39:27.755Z",
        'eventType':"QOS_SUSTAINABILITY",
        'data':{
            'ts': ts,
            'areaInfo':random.choice(networkAreas),
            'startTs': '2023-07-13T08:45:18Z',
            'endTs': '2023-07-13T08:45:18Z',
            'qosFlowRetThd':{
                'relFlowNum': random.randint(0, 100),
                'relTimeUnit': random.choice(["MINUTE", "HOUR", "DAY"]),
                'relFlowRatio':random.randint(0, 100)
            },
            'ranUeThrouThd': "100.0 bps",
            'snssai': random.choice(snssaiss),
            "_5qi": random.randint(0, 10)
        }
    }
    jsons.append(qos_requ_aleatorio)
    col.insert_one(qos_requ_aleatorio)

    qos_requ_aleatorio2 = {
        "owner": "entityA",
        "gdpr_analytics": True,
        "createdAt":"2023-07-21T11:39:27.755Z",
        "updatedAt":"2023-07-21T11:39:27.755Z",
        'eventType':"QOS_SUSTAINABILITY",
        'data':{
            'ts': ts,
            'areaInfo':random.choice(networkAreas),
            'startTs': '2023-07-13T08:45:18Z',
            'endTs': '2023-07-13T08:45:18Z',
            'qosFlowRetThd':{
                'relFlowNum': random.randint(0, 100),
                'relTimeUnit': random.choice(["MINUTE", "HOUR", "DAY"]),
                'relFlowRatio':random.randint(0, 100)
            },
            'ranUeThrouThd': "100.0 bps",
            'snssai': random.choice(snssaiss),
            'gfbr_ul': "10.0 bps",
            'gfbr_dl': "10.0 bps",
            'res_type': "NON_GBR",
            'pdb': 100,
            'per': '1E-1',
            'deviceSpeed': random.choice(devicesSpeeds),
            'deviceType': random.choice(deviceTypes)
        }
    }

    jsons.append(qos_requ_aleatorio2)
    col.insert_one(qos_requ_aleatorio2)

    # ue_mobility_aleatorio = {
    #     "owner": "entityA",
    #     "gdpr_analytics": True,
    #     "createdAt":"2023-07-21T11:39:27.755Z",
    #     "updatedAt":"2023-07-21T11:39:27.755Z",
    #     'eventType':"UE_MOBILITY",
    #     'data':{
    #         'ts': ts,
    #         'supi': "4561230000000000",
    #         'intGroupId': "id300",
    #         'networkArea':random.choice(networkAreas),
    #         'recurringTime':{
    #             'daysOfWeek': [5,2],
    #             'timeOfDayStart':'2023-07-13T08:45:18Z',
    #             'timeOfDayEnd': '2023-07-13T08:45:18Z'
    #         },
    #         'duration': 20,
    #         'durationVariance': 10.4,
    #         'locInfos':[{
    #             'loc': random.choice(locs),
    #             'ratio': 50
    #         }]
    #     }
    # }
    # jsons.append(ue_mobility_aleatorio)
    # col.insert_one(ue_mobility_aleatorio)


#print(jsons)

