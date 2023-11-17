from flask import Flask

def create_app():
    app = Flask(__name__)

    # from .routes import route_1, route_2, ...
    from .routes import index_routes, login_routes

    # app.register_blueprint(page_routes.blueprint_name)
    # app.register_blueprint(...)
    app.register_blueprint(index_routes.index)
    app.register_blueprint(login_routes.login)
    return app