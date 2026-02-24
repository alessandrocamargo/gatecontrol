from flask import Flask, current_app, redirect, url_for, flash, request
from flask_migrate import Migrate

from app.extensions import db, login_manager

migrate = Migrate()


def create_app():
    app = Flask(__name__)

    # Config
    app.config["SECRET_KEY"] = "super-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Flask-Login
    login_manager.login_view = "auth.login"

    # SEMPRE redirecionar para login (evita a página padrão "Please log in...")
    from flask import redirect, request, flash

    @login_manager.unauthorized_handler
    def unauthorized():
        flash("Faça login para continuar.", "warning")
        # Redireciona direto, sem url_for (evita qualquer problema de endpoint)
        return redirect(f"/login?next={request.path}")


    # Helper para o menu não quebrar quando uma rota ainda não existe
    @app.context_processor
    def inject_helpers():
        def has_endpoint(endpoint: str) -> bool:
            return endpoint in current_app.view_functions
        return dict(has_endpoint=has_endpoint)

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

    from app.routes.usuarios import user_bp
    app.register_blueprint(user_bp)

    from app.routes.movimentacao_routes import mov_bp
    app.register_blueprint(mov_bp)


    return app
