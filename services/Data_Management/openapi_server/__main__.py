#!/usr/bin/env python3

import connexion
from flask_apscheduler import APScheduler
from openapi_server import encoder
from openapi_server.db.db import MongoDatabase



def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Nnwdaf_DataManagement'},
                pythonic_params=True)


    client = MongoDatabase()
    app.app.config["db"] = client

    scheduler = APScheduler()
    scheduler.init_app(app.app)
    scheduler.start()
    app.app.config["scheduler"] = scheduler
    app.run(debug=True,port=8080)


if __name__ == '__main__':
    main()
