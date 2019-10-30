# -*- coding: utf-8 -*-

DB_MONGO_USER = 'api_supporter'
DB_MONGO_PASS = 'sampa1621'

# Database Settings
# Connection URI ideal
# MONGO_URI = "mongodb+srv://{}:{}@888-spectate-xmzvt.mongodb.net/" \
#             "test?retryWrites=true&w=majority".format(
#                 os.environ['DB_MONGO_USER'],
#                 os.environ['DB_MONGO_PASS']

# Connection URI for this project
MONGO_URI = "mongodb+srv://{}:{}@888-spectate-xmzvt.mongodb.net/" \
            "test?retryWrites=true&w=majority".format(
                DB_MONGO_USER,
                DB_MONGO_PASS
            )

MONGO_DATABASE = '888-spectate'

DB_FIELDS_RETURN = {
    "_id": 0,
    "id": 1,
    "url": 1,
    "name": 1,
    "startTime": 1
}
