from flask import Flask
from flask_migrate import Migrate
from server.models import db


def create_app():
    app = Flask(__name__)

    #Configuring Sqlalchemy 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    #here we initialize migrate
    Migrate(app, db)

    from server.routes import main
    app.register_blueprint(main)

    return app

if __name__ == '__main__':
    app = create_app()
    # Create database tables for our data models.
    # Hii is equivalent to 'flask db init', 'flask db migrate', and 'flask db upgrade'.
    with app.app_context():
        db.create_all()
    app.run()
