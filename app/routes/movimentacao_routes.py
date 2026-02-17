from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.models.veiculo import Veiculo
from app.models.movimentacao_veiculo import MovimentacaoVeiculo

mov_bp = Blueprint("movimentacao", __name__, url_prefix="/movimentacoes")

@mov_bp.route("/saida", methods=["GET", "POST"])
@login_required
def registrar_saida():

    veiculos = Veiculo.query.all()

    if request.method == "POST":
        veiculo_id = request.form.get("veiculo_id")
        km_saida = request.form.get("km_saida")

        movimentacao_aberta = MovimentacaoVeiculo.query.filter_by(
            veiculo_id=veiculo_id,
            status="em_uso"
        ).first()

        if movimentacao_aberta:
            flash("Este veículo já está em uso.", "error")
            return redirect(url_for("movimentacao.registrar_saida"))

        nova_mov = MovimentacaoVeiculo(
            veiculo_id=veiculo_id,
            km_saida=km_saida,
            operador_saida_id=current_user.id
        )
        veiculo = Veiculo.query.get(veiculo_id)
        veiculo.status = "em_uso"

        db.session.add(nova_mov)
        db.session.commit()

        flash("Saída registrada com sucesso!", "success")
        return redirect(url_for("veiculo.listar_veiculos"))

    return render_template("saida_form.html", veiculos=veiculos)

@mov_bp.route("/entrada/<int:id>", methods=["GET", "POST"])
@login_required
def registrar_retorno(id):

    movimentacao = MovimentacaoVeiculo.query.get_or_404(id)

    if request.method == "POST":
        km_retorno = request.form.get("km_retorno")

        if int(km_retorno) < movimentacao.km_saida:
            flash("KM entrada não pode ser menor que KM saída.", "error")
            return redirect(request.url)

        movimentacao.km_retorno = km_retorno
        movimentacao.operador_retorno_id = current_user.id
        movimentacao.status = "finalizado"

        db.session.commit()

        flash("Retorno registrado com sucesso!", "success")
        return redirect(url_for("veiculo.listar_veiculos"))

    return render_template("entrada_form.html", movimentacao=movimentacao)
