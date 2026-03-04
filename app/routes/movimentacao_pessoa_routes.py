from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_required, current_user
from app.extensions import db
from app.models.pessoa import Pessoa
from app.models.movimentacao_pessoa import MovimentacaoPessoa, STATUS_DENTRO, STATUS_SAIU
from app.services.movimentacao_pessoa_service import registrar_entrada_pessoa, registrar_saida_pessoa, RegraNegocioError

pessoa_mov_bp = Blueprint("movimentacao_pessoa", __name__, url_prefix="/movimentacoes-pessoa")

# =================================
# FORM ENTRADA
# =================================
@pessoa_mov_bp.route("/entrada", methods=["GET"])
@login_required
def form_entrada():
    return render_template("pessoa_entrada.html")

# =================================
# REGISTRAR ENTRADA
# =================================
@pessoa_mov_bp.route("/entrada", methods=["POST"])
@login_required
def registrar_entrada():
    nome = request.form.get("nome")
    documento = request.form.get("documento")
    tipo = request.form.get("tipo")
    setor_id = request.form.get("setor_id")

    if not nome or not documento:
        flash("Nome e são obrigatórios.", "warning")
        return redirect(url_for("movimentacao_pessoa.form_entrada"))
    
    # procurar pessoa
    pessoa = Pessoa.query.filter_by(documento=documento).first()

    # senão existir criar
    if not pessoa:
        pessoa = Pessoa(
            nome = nome,
            documento = documento,
            tipo = tipo,
            setor_id = setor_id
        )

        db.session.add(pessoa)
        db.session.commit()
    
    try:
        registrar_entrada_pessoa(
            pessoa_id = pessoa.id,
            operador_id = current_user.id
        )
        flash("Entrada registrada com sucesso.", "success")
    except RegraNegocioError as e:
        flash(str(e), "warning")
    return redirect(url_for("main.home"))

# =================================
# REGISTRAR SAIDA
# =================================
@pessoa_mov_bp.route("/saida/<int:id>", methods=["POST"])
@login_required
def registrar_saida(id):
    try:
        registrar_saida_pessoa(
            mov_id = id,
            operador_id = current_user.id
        )
        flash("Saida registrada com sucesso.", "success")
    except RegraNegocioError as e:
        flash(str(e), "warning")
    return redirect(url_for("main.home"))