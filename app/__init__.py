from flask import Flask

def create_app():
    app = Flask(__name__)

    # from .routes import route_1, route_2, ...
    from .routes import index_routes,settings_routes,profile_routes,listing_routes

    # app.register_blueprint(page_routes.blueprint_name)
    # app.register_blueprint(...)
    app.register_blueprint(index_routes.index)
    app.register_blueprint(settings_routes.settings)
    app.register_blueprint(profile_routes.profile)
    app.register_blueprint(listing_routes.listing)

    return app