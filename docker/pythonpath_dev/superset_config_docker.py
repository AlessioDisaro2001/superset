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

from logging.handlers import RotatingFileHandler
import logging

LOG_LEVEL = 'DEBUG'
LOG_FORMAT = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
SUPERSET_LOG_DIR = '/app/superset/log/superset.log'

handler = RotatingFileHandler(SUPERSET_LOG_DIR, maxBytes=10000000, backupCount=5)
handler.setLevel(LOG_LEVEL)
handler.setFormatter(logging.Formatter(LOG_FORMAT))
logging.getLogger().addHandler(handler)
