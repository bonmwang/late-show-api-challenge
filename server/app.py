from flask import Flask
from server.extensions import db, migrate, jwt
from server.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)  
    jwt.init_app(app)

    # Register blueprints
    from server.controllers.auth_controller import auth_bp
    from server.controllers.movie_controller import movie_bp
    from server.controllers.show_controller import show_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(movie_bp)
    app.register_blueprint(show_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)