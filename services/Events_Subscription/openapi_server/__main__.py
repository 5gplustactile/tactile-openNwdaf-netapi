#!/usr/bin/env python3

import connexion
import ssl
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from openapi_server import encoder
from openapi_server.db.db import MongoDatabase
from datetime import datetime
import logging



def main():

    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Nnwdaf_EventsSubscription'},
                pythonic_params=True)

    client = MongoDatabase()
    app.app.config["db"] = client

    jobstores = {
        'default': MongoDBJobStore(database='apscheduler', collection='jobs', client=client.client)
    }
    scheduler = BackgroundScheduler(jobstores=jobstores)
    scheduler.start()

    app.app.config["scheduler"] = scheduler


    app.run(debug=True, port=8080, use_reloader=False)


if __name__ == '__main__':
    main()
