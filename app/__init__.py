from flask import Flask
import os 
from dotenv import load_dotenv
from .database import db
from sqlalchemy import text



def create_app():
    app = Flask(__name__)
    
    load_dotenv()

    #database connection
    app.config["SQLALCHEMY_DATABASE_URI"] = \
    f'postgresql://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'
    app.config['SQLAlCHEMY_ECHO'] = True

    db.init_app(app)

    #Validate database connection
    with app.app_context():
        try:
            db.session.execute(text('SELECT 1'))
            print('Successful connection')
        except Exception as e:
            print(f"Connection failed. ERROR:{e}")



    # from .routes import route_1, route_2, ...
    from .routes import index_routes,settings_routes,profile_routes,listing_routes

    # app.register_blueprint(page_routes.blueprint_name)
    # app.register_blueprint(...)
    app.register_blueprint(index_routes.index)
    app.register_blueprint(settings_routes.settings)
    app.register_blueprint(profile_routes.profile)
    app.register_blueprint(listing_routes.listing)

    return app