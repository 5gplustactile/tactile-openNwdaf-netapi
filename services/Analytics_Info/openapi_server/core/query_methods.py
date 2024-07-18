from flask import current_app


def add_and(q, d):
    if "$and" in q:
        q["$and"].append(d)
    else:
        q["$and"] = []
        q["$and"].append(d)
    return q

def search(q, d, event):
    
    collection = current_app.config["db"].get_coll("analytics") 
    res = list(collection.find(q, {"_id":0}))
    data = []
    for r in res:
        data.append(r["data"])
    return data

def query_snssais(snssais, atributo):
    and_conditions_list = []
    for snssai in snssais:
        condition = {}
        for key, value in snssai.to_dict().items():
            if value is not None:
                condition[f"data.{atributo}.{key}"] = value
        and_conditions_list.append(condition)
    
    return and_conditions_list

def query_network_areas(network_areas, network_key, atributo):
    and_conditions_list=[]
    if network_areas is not None:
        for i in network_areas:
            condition = {}
            for key, value in i.items():
                if value is not None:
                    if key == "plmnId":
                        plmn_condition = {}
                        for plmn_key, plmn_value in value.items():
                            plmn_condition[f"data.{atributo}.{network_key}.plmnId.{plmn_key}"] = plmn_value
                        condition.update(plmn_condition)
                    elif key == "gNbId":
                        g_nb_condition = {}
                        for g_nb_key, g_nb_value in value.items():
                            g_nb_condition[f"data.{atributo}.{network_key}.gNbId.{g_nb_key}"] = g_nb_value
                        condition.update(g_nb_condition)
                    else:
                        condition[f"data.{atributo}.{network_key}.{key}"] = value
            and_conditions_list.append(condition)
    return and_conditions_list

def query_loc(locs):
    and_conditions_list=[]
    if locs is not None:
        for i in locs:
            or_condition = {}
            for key, value in i.items():
                if value is not None:
                    condition = {}
                    for key2, value2 in value.items():
                        if value2 is not None:
                            if key2 =="ecgi" or key2 == "utraLocation" or key2 == "sai" or key2 == "lai" or key2 == "rai" or key2 == "tai" or key2 =="n3gppTai" or key2 =="cgi" or key2 =="n3gppTai" or key2 == "ncgi":
                                ecgi_condition={}
                                for ecgi_key, ecgi_value in value2.items():
                                    if ecgi_key=="plmnId":
                                        plmn_condition = {}
                                        for plmn_key, plmn_value in ecgi_value.items():
                                            plmn_condition[f"data.loc.{key}.{key2}.plmnId.{plmn_key}"] = plmn_value
                                        ecgi_condition.update(plmn_condition)
                                    else:
                                        ecgi_condition[f"data.loc.{key}.{key2}.tai.{ecgi_key}"]=ecgi_value
                                condition.update(ecgi_condition)
                            elif key2 == "globalNgenbId" or key2 == "globalENbId" or key2 == "globalGnbId":
                                globalNgenbId_condition = {}
                                for globalNgenbId_key, globalNgenbId_value in value2.items():
                                    if globalNgenbId_key=="plmnId":
                                        plmn_condition = {}
                                        for plmn_key, plmn_value in globalNgenbId_value.items():
                                            plmn_condition[f"data.loc.{key}.{key2}.plmnId.{plmn_key}"] = plmn_value
                                        globalNgenbId_condition.update(plmn_condition)
                                    elif globalNgenbId_key == "gNbId":
                                        gNbId_condition = {}
                                        for gNbId_key, gNbId_value in globalNgenbId_value.items():
                                            gNbId_condition[f"data.loc.{key}.{key2}.gNbId.{gNbId_key}"] = gNbId_value
                                        globalNgenbId_condition.update(gNbId_condition)
                                    else:
                                        globalNgenbId_condition[f"data.loc.{key}.{key2}.{globalNgenbId_key}"]=globalNgenbId_value
                                condition.update(globalNgenbId_condition)
                            elif key2 == "tnapId" or key2 =="twapId" or key2 == "hfcNodeId":
                                tnapId_condition = {}
                                for tnapId_key, tnapId_value in value2.items():
                                    tnapId_condition [f"data.loc.{key}.{key2}.{tnapId_key}"]=tnapId_value
                                condition.update(tnapId_condition )
                            else:
                                condition[f"data.loc.{key}.{key2}"] = value
                or_condition.update(condition)
            and_conditions_list.append(or_condition)
    return and_conditions_list


def query_qos_requ(qos_requ):
    and_conditions_list = []
    condition = {}
    for key, value in qos_requ.to_dict().items():
        if value is not None:
            if key == "deviceSpeed":
                device_condition = {}
                for device_key, device_value in value.items():
                    device_condition[f"data.deviceSpeed.{device_key}"] = device_value
                condition.update(device_condition)
            else:
                condition[f"data.{key}"] = value
    and_conditions_list.append(condition)
    return and_conditions_list