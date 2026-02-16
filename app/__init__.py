from flask import Flask
from app.extensions import db, login_manager


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "super-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"

    # Importar models depois de inicializar db
    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Registrar blueprints
    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)

    from app.routes.main_routes import main_bp
    app.register_blueprint(main_bp)


    return app
