# -*- coding: utf-8 -*-

JSON_NEW_EVENT = {
   "id": 8661032861909884224,
   "message_type": "NewEvent",
   "event": {
      "id": 994839351740,
      "name": "Real Madrid vs Barcelona",
      "startTime": "2018-06-20 10:30:00",
      "sport": {
         "id": 221,
         "name": "Football"
      },
      "markets": [
         {
            "id": 385086549360973392,
            "name": "Winner",
            "selections": [
               {
                  "id": 8243901714083343527,
                  "name": "Real Madrid",
                  "odds": 1.01
               },
               {
                  "id": 5737666888266680774,
                  "name": "Barcelona",
                  "odds": 1.01
               }
            ]
         }
      ]
   }
}

JSON_NEW_EVENT_02 = {
   "id": 8661032861909881111,
   "message_type": "UpdateOdds",
   "event": {
      "id": 994839351722,
      "name": "Real Madrid vs Barcelona 02",
      "startTime": "2018-06-20 10:30:00",
      "sport": {
         "id": 221,
         "name": "Football"
      },
      "markets": [
         {
            "id": 385086549360973392,
            "name": "Winner",
            "selections": [
               {
                  "id": 8243901714083343527,
                  "name": "Real Madrid",
                  "odds": 12.00
               },
               {
                  "id": 5737666888266680774,
                  "name": "Barcelona",
                  "odds": 53.55
               }
            ]
         }
      ]
   }
}

JSON_UPDATE_ODDS = {
   "id": 8661032861909884224,
   "message_type": "UpdateOdds",
   "event": {
      "id": 994839351740,
      "name": "Real Madrid vs Barcelona",
      "startTime": "2018-06-20 10:30:00",
      "sport": {
         "id": 221,
         "name": "Football"
      },
      "markets": [
         {
            "id": 385086549360973392,
            "name": "Winner",
            "selections": [
               {
                  "id": 8243901714083343527,
                  "name": "Real Madrid",
                  "odds": 10.00
               },
               {
                  "id": 5737666888266680774,
                  "name": "Barcelona",
                  "odds": 5.55
               }
            ]
         }
      ]
   }
}

JSON_ALL_MATCHS = [
    {
        "url": "/api/v1/match/8661032861909884224",
        "sport": {
            "id": 221,
            "name": "Football"
        },
        "startTime": "2018-06-20 10:30:00",
        "name": "Real Madrid vs Barcelona",
        "markets": [
            {
                "id": 385086549360973392,
                "name": "Winner",
                "selections": [
                    {
                        "odds": 5.0,
                        "id": 8243901714083343527,
                        "name": "Real Madrid"
                    },
                    {
                        "odds": 2.55,
                        "id": 5737666888266680774,
                        "name": "Barcelona"
                    }
                ]
            }
        ],
        "id": 8661032861909884224
    },
    {
        "url": "/api/v1/match/8661032861909881111",
        "sport": {
            "id": 221,
            "name": "Football"
        },
        "startTime": "2018-06-20 10:30:00",
        "name": "Real Madrid vs Barcelona",
        "markets": [
            {
                "id": 385086549360973392,
                "name": "Winner",
                "selections": [
                    {
                        "odds": 12.0,
                        "id": 8243901714083343527,
                        "name": "Real Madrid"
                    },
                    {
                        "odds": 53.55,
                        "id": 5737666888266680774,
                        "name": "Barcelona"
                    }
                ]
            }
        ],
        "id": 8661032861909881111
    }
]

JSON_EVENT_BY_ID = {
    "sport": {
        "id": 221,
        "name": "Football"
    },
    "markets": [
        {
            "selections": [
                {
                    "id": 8243901714083343527,
                    "odds": 1.01,
                    "name": "Real Madrid"
                },
                {
                    "id": 5737666888266680774,
                    "odds": 1.01,
                    "name": "Barcelona"
                }
            ],
            "id": 385086549360973392,
            "name": "Winner"
        }
    ],
    "url": "/api/v1/match/994839351740",
    "id": 994839351740,
    "name": "Real Madrid vs Barcelona",
    "startTime": "2018-06-20 10:30:00"
}

JSON_EVENT_BY_NAME = {
    "name": "Real Madrid vs Barcelona",
    "startTime": "2018-06-20 10:30:00",
    "id": 994839351740,
    "url": "/api/v1/match/994839351740"
}

JSON_EVENT_BY_SPORT = [
    {
        "url": "/api/v1/match/994839351740",
        "id": 994839351740,
        "name": "Real Madrid vs Barcelona",
        "startTime": "2018-06-20 10:30:00"
    }
]
