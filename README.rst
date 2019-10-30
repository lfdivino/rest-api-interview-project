# 888-spectate-interview-project

#### Motivation:

Betbright is a sports betting platform. The main functional areas are:
- Manage data about sporting events to allow users to place bets.
- Provide API to receive data from external providers and update our system with the latest data about events in real time.
- Provide access to support team to allow the to see the most recent data for each event and to query data.

Tech Stack
======================

For this API were chosen as stack:

- Flask
- Flask Restful
- MongoDB (Atlas_)
- Pymongo
- Docker

Install
==========

First of all clone this project and access it's root folder

1 - Install with virtualenv
=================================

To install using a virtualenv environment just use the command ::

    ./fast_install.sh

After the installation active the virtualenv ::

    source venv/bin/activate

Then just start the API ::

    api_888_interview/api.py

To test the api just use the following command ::

    python3 api_888_interview/test/test_event.py

2 - API Docker Installation
=========================

To install the API using docker just follow the command (Assuming you have Docker installed previously) ::

    sudo docker build --no-cache -t api_888 .
    sudo docker run -it -p 5000:5000 api_888

So inside the container just use the following commands to execute the API or execute its tests ::

    python api/api_888_interview/api.py
    python api/api_888_interview/test/test_event.py

API Routes
============

The API Routes:

- POST '/api/v1/event'
- POST '/api/v1/odds'
- GET  '/api/v1/match/<event_id>'
- GET  '/api/v1/match/' (The Querystring parameters can be use: 'name', 'sport', 'ordering')

Maintainers
-----------

- Luiz_ Felipe_ Divino_ (owner)

.. Deputados Crawler links
.. _Website: http://www.camara.leg.br/internet/deputado/Dep_Lista_foto.asp?Legislatura=55&Partido=QQ&SX=QQ&Todos=None&UF=QQ&condic=QQ&forma=lista&nome=&ordem=nome&origem=None

.. Ferramentas Utilizadas links
.. _Atlas: https://cloud.mongodb.com/

.. Maintainers links
.. _Luiz: https://github.com/lfdivino
.. _Felipe: https://github.com/lfdivino
.. _Divino: https://github.com/lfdivino