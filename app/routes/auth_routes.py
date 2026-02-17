from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user
from app.models.user import User
from app.extensions import db
from app.utils.decorators import admin_required

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    # para redirecionar o usuário de volta à página que ele tentou acessar
    next_url = request.args.get("next")

    if request.method == "POST":
        username = (request.form.get("username") or "").strip().lower()
        password = request.form.get("password") or ""

        user = User.query.filter_by(username=username).first()

        if user and user.ativo and user.check_password(password):
            login_user(user)
            flash(f"Bem-vindo, {user.username}!", "success")
            return redirect(next_url or url_for("main.home"))

        flash("Usuário ou senha inválidos (ou usuário inativo).", "danger")

    return render_template("auth/login.html", next_url=request.args.get("next"))


@auth_bp.route("/logout")
def logout():
    logout_user()
    flash("Você saiu do sistema.", "success")
    return redirect(url_for("auth.login"))


@auth_bp.route("/register", methods=["POST"])
@admin_required
def register():
    data = request.get_json() or {}

    username = (data.get("username") or "").strip().lower()
    password = data.get("password")
    role = (data.get("role") or "operador").strip().lower()

    if not username or not password:
        return jsonify({"erro": "Username e password são obrigatórios"}), 400

    if role not in ("admin", "cadastro", "operador"):
        return jsonify({"erro": "Role inválida"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"erro": "Usuário já existe"}), 400

    new_user = User(nome=username, username=username, role=role, ativo=True)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"mensagem": "Usuário criado com sucesso"}), 201
