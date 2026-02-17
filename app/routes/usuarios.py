from flask import Blueprint, render_template, request, redirect, url_for, flash

from app.extensions import db
from app.models.user import User
from app.utils.decorators import admin_required

# Nome do blueprint = user
user_bp = Blueprint("user", __name__, url_prefix="/usuarios")


@user_bp.route("/novo", methods=["GET", "POST"])
@admin_required
def novo_usuario():

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        username = request.form.get("username", "").strip().lower()
        role = request.form.get("role", "operador").strip().lower()
        senha = request.form.get("senha", "")
        senha2 = request.form.get("senha2", "")
        ativo = True if request.form.get("ativo") == "on" else False

        # validações
        if not nome or not username or not senha or not senha2:
            flash("Preencha todos os campos obrigatórios.", "danger")
            return render_template("usuarios/novo.html")

        if senha != senha2:
            flash("As senhas não conferem.", "danger")
            return render_template("usuarios/novo.html")

        if len(senha) < 6:
            flash("A senha deve ter no mínimo 6 caracteres.", "danger")
            return render_template("usuarios/novo.html")

        if role not in ("admin", "cadastro", "operador"):
            flash("Permissão inválida.", "danger")
            return render_template("usuarios/novo.html")

        # username único
        if User.query.filter_by(username=username).first():
            flash("Já existe um usuário com esse login.", "warning")
            return render_template("usuarios/novo.html")

        user = User(
            nome=nome,
            username=username,
            role=role,
            ativo=ativo
        )

        user.set_password(senha)

        db.session.add(user)
        db.session.commit()

        flash("Usuário criado com sucesso!", "success")

        # IMPORTANTE: endpoint correto
        return redirect(url_for("user.novo_usuario"))

    return render_template("usuarios/novo.html")
