from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from dotenv import load_dotenv

import os

db = SQLAlchemy()
#login_manager = LoginManager()
migrate = Migrate()

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Registro de rota
    
    from .routes.registro_routes import registro_bp
    app.register_blueprint(registro_bp)
    
    from .routes.veiculo_routes import veiculo_bp
    app.register_blueprint(veiculo_bp)

    from .routes.setor_routes import setor_bp
    app.register_blueprint(setor_bp)
    
    from .routes.pessoa_route import pessoa_bp
    app.register_blueprint(pessoa_bp)


    db.init_app(app)
    #login_manager.init_app(app)
    migrate.init_app(app, db)

    return app