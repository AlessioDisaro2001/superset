#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#
# This is an example "local" configuration file. In order to set/override config
# options that ONLY apply to your local environment, simply copy/rename this file
# to docker/pythonpath/superset_config_docker.py
# It ends up being imported by docker/superset_config.py which is loaded by
# superset/config.py
#

# SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://pguser:pgpwd@some.host/superset"
# SQLALCHEMY_ECHO = True

from celery.schedules import crontab
from logging.handlers import RotatingFileHandler
import logging

LOG_LEVEL = 'DEBUG'
LOG_FORMAT = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
SUPERSET_LOG_DIR = '/app/superset/log/superset.log'

handler = RotatingFileHandler(SUPERSET_LOG_DIR, maxBytes=10000000, backupCount=5)
handler.setLevel(LOG_LEVEL)
handler.setFormatter(logging.Formatter(LOG_FORMAT))
logging.getLogger().addHandler(handler)

ALERT_REPORTS_NOTIFICATION_DRY_RUN = False

FEATURE_FLAGS = {
    "ALERT_REPORTS": True,
    "ALLOW_FULL_CSV_EXPORT": True
}

REDIS_HOST = "superset_cache"
REDIS_PORT = "6379"

class CeleryConfig:
    broker_url = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
    imports = (
        "superset.sql_lab",
        "superset.tasks.scheduler",
    )
    result_backend = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
    worker_prefetch_multiplier = 10
    task_acks_late = True
    task_annotations = {
        "sql_lab.get_sql_results": {
            "rate_limit": "100/s",
        },
    }
    beat_schedule = {
        "reports.scheduler": {
            "task": "reports.scheduler",
            "schedule": crontab(minute="*", hour="*"),
        },
        "reports.prune_log": {
            "task": "reports.prune_log",
            "schedule": crontab(minute=0, hour=0),
        },
    }
CELERY_CONFIG = CeleryConfig

SCREENSHOT_LOCATE_WAIT = 100
SCREENSHOT_LOAD_WAIT = 600

# Email configuration
SMTP_HOST = "smtp.gmail.com" # change to your host
SMTP_PORT = 587 # your port, e.g. 587
SMTP_STARTTLS = True
SMTP_SSL_SERVER_AUTH = True # If you're using an SMTP server with a valid certificate
SMTP_SSL = False
SMTP_USER = "..." # use the empty string "" if using an unauthenticated SMTP server
SMTP_PASSWORD = "..." # use the empty string "" if using an unauthenticated SMTP server
SMTP_MAIL_FROM = "noreply@....com"
EMAIL_REPORTS_SUBJECT_PREFIX = "[Superset] " # optional - overwrites default value in config.py of "[Report] "

# This is for internal use, you can keep http
WEBDRIVER_BASEURL = "http://superset_app:8088" # When running using docker compose use "http://superset_app:8088'
# This is the link sent to the recipient. Change to your domain, e.g. https://superset.mydomain.com
WEBDRIVER_BASEURL_USER_FRIENDLY = "http://localhost:8088"

# Set a minimum interval threshold between executions (for each Alert/Report)
# Value should be an integer
# ALERT_MINIMUM_INTERVAL = int(timedelta(minutes=10).total_seconds())
# REPORT_MINIMUM_INTERVAL = int(timedelta(minutes=5).total_seconds())
