from flask import Flask

def create_app():
    app = Flask(__name__)

    # from .routes import route_1, route_2, ...

    # app.register_blueprint(route_1)
    # app.register_blueprint(...)

    return app