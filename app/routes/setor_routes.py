from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.extensions import db
from app.models.setor import Setor
from app.utils.decorators import admin_required

setor_bp = Blueprint("setor", __name__, url_prefix="/setores")


# ==========================
# LISTAR SETORES
# ==========================
@setor_bp.route("/")
@login_required
def listar_setores():
    setores = Setor.query.order_by(Setor.id.desc()).all()
    return render_template("setor_list.html", setores=setores)


# ==========================
# CRIAR SETOR
# ==========================
@setor_bp.route("/criar", methods=["GET", "POST"])
@admin_required
def criar_setor():
    if request.method == "POST":
        nome = request.form.get("nome")

        if not nome:
            flash("O nome do setor é obrigatório.", "error")
            return redirect(url_for("setor.criar_setor"))

        setor_existente = Setor.query.filter_by(nome=nome).first()

        if setor_existente:
            flash("Já existe um setor com esse nome.", "error")
            return redirect(url_for("setor.criar_setor"))

        novo_setor = Setor(nome=nome)
        db.session.add(novo_setor)
        db.session.commit()

        flash("Setor cadastrado com sucesso!", "success")
        return redirect(url_for("setor.listar_setores"))

    return render_template("setor_form.html")


# ==========================
# EXCLUIR SETOR
# ==========================
@setor_bp.route("/excluir/<int:id>")
@admin_required
def excluir_setor(id):
    setor = Setor.query.get_or_404(id)

    db.session.delete(setor)
    db.session.commit()

    flash("Setor excluído com sucesso!", "success")
    return redirect(url_for("setor.listar_setores"))
