# -*- coding: utf-8 -*-
"""
    wsgi
    ~~~~

    entrypoint wsgi script
"""

from api import app
from werkzeug.serving import run_simple

application = app.create_app()

if __name__ == "__main__":
    run_simple(
        '0.0.0.0', 5000, application, use_reloader=False, use_debugger=True
    )
