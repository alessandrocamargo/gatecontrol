from flask import Blueprint, request, jsonify, render_template, flash, redirect, url_for
from app import db
from app.models.pessoa import Pessoa
from app.models.setor import Setor
from flask_login import login_required

pessoa_bp = Blueprint("pessoa", __name__, url_prefix="/pessoas")


# =========================
# Criar Pessoa
# =========================
@pessoa_bp.route("/criar", methods=["GET", "POST"])
@login_required
def criar_pessoa():
    setores = Setor.query.all()

    if request.method == "POST":
        nome = request.form.get("nome")
        documento = request.form.get("documento")
        tipo = request.form.get("tipo")
        setor_id = request.form.get("setor_id")

        if not nome or not documento or not tipo or not setor_id:
            flash("Todos os campos são obrigatórios.", "error")
            return redirect(url_for("pessoa.criar_pessoa"))

        pessoa_existente = Pessoa.query.filter_by(documento=documento).first()
        if pessoa_existente:
            flash("Já existe uma pessoa com esse documento.", "error")
            return redirect(url_for("pessoa.criar_pessoa"))

        nova_pessoa = Pessoa(
            nome=nome,
            documento=documento,
            tipo=tipo,
            setor_id=setor_id
        )

        db.session.add(nova_pessoa)
        db.session.commit()

        flash("Pessoa cadastrada com sucesso!", "success")
        return redirect(url_for("pessoa.listar_pessoas"))

    return render_template("pessoaForm.html", setores=setores)



# =========================
# Listar Pessoas
# =========================
@pessoa_bp.route("/")
@login_required
def listar_pessoas():
    pessoas = Pessoa.query.order_by(Pessoa.id.desc()).all()
    return render_template("pessoa_list.html", pessoas=pessoas)



# =========================
# FORMULARIO PESSOA
# =========================
@pessoa_bp.route("/pessoa/form", methods=["GET"])
def form_pessoa():
    return render_template("pessoaForm.html")
