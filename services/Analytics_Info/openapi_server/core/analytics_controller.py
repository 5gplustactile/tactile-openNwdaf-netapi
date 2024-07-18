from ..db.db import MongoDatabase
from ..core.statistics import statistics
from ..core.prediction import prediction
from ..models.event_reporting_requirement import EventReportingRequirement
from ..models.analytics_data import AnalyticsData
from ..core.responses import bad_request_error, make_response, internal_server_error, not_found_error
from datetime import datetime
from flask import current_app

class analytics_controller:

    stats = statistics()
    predict = prediction()
    def get_requests(self, event_id, ana_req:EventReportingRequirement=None, event_filter=None, supported_features=None, tgt_ue=None):
        #Depending on the dates given in ana_req, we return statistical data or make a prediction

        current_app.logger.debug(f"{ana_req=}")
        d = {"start":datetime.now().isoformat("T", "milliseconds"), 
            "expiry":datetime.now().isoformat("T", "milliseconds"),
            "timeStampGen":datetime.now().isoformat("T", "milliseconds")
        }

        #Statistics search path
        try:
            if ana_req.start_ts.isoformat("T", "milliseconds") < datetime.now().isoformat("T", "milliseconds") and ana_req.end_ts.isoformat("T", "milliseconds") < datetime.now().isoformat("T", "milliseconds"):
                current_app.logger.debug("STATISTICS PATH")
                try:
                    datos = AnalyticsData().from_dict(d)
                    r = self.stats.get_stats(d=datos, event=event_id, ana_req=ana_req, event_filter=event_filter, supported_features=supported_features, tgt_ue=tgt_ue)
                    res = make_response(r, status=200)
                except Exception as e:
                    current_app.logger.debug(f"Error: {e}")
                    if str(e.args[0]==204):
                        return make_response("No Content", 204)
                    else:
                        return bad_request_error("Some attributes are not right", cause=e.args[1], invalid_params=e.args[0])
            
            #Data prediction path
            elif ana_req.start_ts.isoformat("T", "milliseconds") > datetime.now().isoformat("T", "milliseconds") and ana_req.end_ts.isoformat("T", "milliseconds") > datetime.now().isoformat("T", "milliseconds"):
                current_app.logger.debug("PREDICTION PATH")
                try:
                    datos = AnalyticsData().from_dict(d)
                    r = self.predict.get_pred(d=datos, event=event_id, ana_req=ana_req, event_filter=event_filter, supported_features=supported_features, tgt_ue=tgt_ue)
                    current_app.logger.debug("END PREDICTION PATH")
                    res = make_response(r, status=200)
                except Exception as e:
                    current_app.logger.debug(f"Error: {e}")
                    if str(e.args[0]==204):
                        return make_response("No Content", 204)
                    else:
                        return bad_request_error("Some attributes are not right", cause=e.args[1], invalid_params=e.args[0])
            

            #Bad Request path (past and future dates)
            else:
                res = bad_request_error(detail="Start time in the past and the end time in the future", cause="BOTH_STAT_PRED_NOT_ALLOWED", invalid_params="startTs endTs")
            return res
        except Exception as e:
            exception = "An exception occurred in get analytics"
            current_app.logger.error(exception + "::" + str(e))
            return e