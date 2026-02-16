from flask import Blueprint,render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from app.extensions import db
from app.utils.decorators import admin_required

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash(f"Bem-vindo, {user.username}!", "success")
            return redirect(url_for("main.home"))
        else:
            flash("Usuário ou senha inválidos", "error")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    logout_user()
    flash("Você saiu do sistema." , "sucess")
    return redirect(url_for("auth.login"))

@auth_bp.route("/register", methods=["POST"])
@admin_required
def register():
    data = request.get_json() or {}

    username = data.get("username")
    password = data.get("password")
    role = data.get("role", "operador")

    if not username or not password:
        return jsonify({"erro": "Username e password são obrigatórios"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"erro": "Usuário já existe"}), 400

    new_user = User(username=username, role=role)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"mensagem": "Usuário criado com sucesso"}), 201
