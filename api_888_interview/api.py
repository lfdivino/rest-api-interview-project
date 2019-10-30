# -*- coding: utf-8 -*-
from werkzeug.serving import run_simple
from api_888_interview.app import core

if __name__ == '__main__':
    app = core.core_app()
    run_simple('0.0.0.0', 5000, app, use_reloader=True)
