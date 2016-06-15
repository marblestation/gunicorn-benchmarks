# encoding: utf-8
"""
Application factory
"""

import logging.config

from flask import Flask
from flask.ext.restful import Api
from views import BenchmarkView, ServiceView, ServiceView2


def create_app():
    """
    Create the application and return it to the user
    :return: application
    """

    app = Flask(__name__, static_folder='static')
    app.url_map.strict_slashes = False

    # Load config and logging
    load_config(app)
    logging.config.dictConfig(
        app.config['LOGGING']
    )

    # Register extensions
    api = Api(app)

    # Add the end resource end points
    api.add_resource(BenchmarkView, '/benchmark/<int:sleep>', methods=['GET'])
    api.add_resource(ServiceView, '/service/<int:sleep>', methods=['GET'])
    api.add_resource(ServiceView2, '/service2/<int:sleep>', methods=['GET'])
    return app


def load_config(app):
    """
    Loads configuration in the following order:
        1. config.py
        2. local_config.py (ignore failures)
        3. consul (ignore failures)
    :param app: flask.Flask application instance
    :return: None
    """

    app.config.from_pyfile('config.py')

    try:
        app.config.from_pyfile('local_config.py')
    except IOError:
        app.logger.warning('Could not load local_config.py')


if __name__ == '__main__':
    running_app = create_app()
    running_app.run(debug=True, use_reloader=False)
