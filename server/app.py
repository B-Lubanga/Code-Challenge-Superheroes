from flask import Flask
from flask_migrate import Migrate
from server.models import db


def create_app():
    # This tells Flask where to find HTML templates and static files like videos
    app = Flask(__name__, static_folder='static', template_folder='templates')

    #Configuring Sqlalchemy 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize database
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
    app.run(debug=True)
