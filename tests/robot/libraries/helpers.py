
import re
import urllib.parse

def get_subscriber_and_subscription_from_location(input):
    p = re.compile('^.*/v1/([a-zA-Z0-9]+)/subscriptions/([a-zA-Z0-9]+)/?')
    m = p.match(input)
    if m:
        if m.lastindex == 2:
            return m[1], m[2]
        raise Exception('Only match ' + m.lastindex + ' and the expected is 2')
    else:
        raise Exception('Host is not present at ' + input)

def get_endpoint_from_dict(event, ana_req, event_filter={}, tgt_ue={}):
    data={
        "event-id": event,
        "ana-req":ana_req,
        "tgt-ue":tgt_ue,
        "event-filter":event_filter
    }
    url_encoded_data = urllib.parse.urlencode(data, quote_via=urllib.parse.quote)
    url="/nnwdaf-analyticsinfo/v1/analytics?"+url_encoded_data.replace("%27", '%22')
    return url

def check_result(d):
    return True

