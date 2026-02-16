from flask import Flask
from app.extensions import db, login_manager
from flask_migrate import Migrate


migrate = Migrate()
def create_app():
    app = Flask(__name__)
    migrate.init_app(app,db)
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

    from app.routes.setor_routes import setor_bp
    app.register_blueprint(setor_bp)

    from app.routes.pessoa_routes import pessoa_bp
    app.register_blueprint(pessoa_bp)

    from app.routes.veiculo_routes import veiculo_bp
    app.register_blueprint(veiculo_bp)





    return app
