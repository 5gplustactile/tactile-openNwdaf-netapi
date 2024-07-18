from flask_apscheduler import APScheduler

scheduler = APScheduler()

def configure_scheduler(app):
    scheduler.init_app(app)
    scheduler.start()

    from .core.controller_notifications import __periodic_notifications__

    return scheduler
