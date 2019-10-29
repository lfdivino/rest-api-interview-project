# -*- coding: utf-8 -*-
import os

os.environ

# Database Settings
MONGO_URI = "mongodb+srv://{}:{}@888-spectate-xmzvt.mongodb.net/" \
            "test?retryWrites=true&w=majority".format(
                os.environ['DB_MONGO_USER'],
                os.environ['DB_MONGO_PASS']
            )
MONGO_DATABASE = '888-spectate'
