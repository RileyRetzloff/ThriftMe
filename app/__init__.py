from flask import Flask

def create_app():
    app = Flask(__name__)

    # from .routes import route_1, route_2, ...
    from .routes import (
        index_routes, # Riley
        login_routes,
        profile_routes,
        settings_routes,
        sell_routes, # Riley
        listing_routes, # Riley
        community_routes,
        contact_routes,
        user_routes,
        marketplace_routes
    )
    
    app.register_blueprint(index_routes.index)
    app.register_blueprint(login_routes.login)
    app.register_blueprint(profile_routes.profile)
    app.register_blueprint(settings_routes.settings)
    app.register_blueprint(sell_routes.sell)
    app.register_blueprint(listing_routes.listing)
    app.register_blueprint(community_routes.community)
    app.register_blueprint(contact_routes.contact)
    app.register_blueprint(user_routes.user)
    app.register_blueprint(marketplace_routes.marketplace)
    
    return app