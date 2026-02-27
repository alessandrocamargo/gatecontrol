from flask import Blueprint, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app.services.movimentacao_service import (
    registrar_saida_service,
    registrar_retorno_service,
    RegraNegocioError,
)

mov_bp = Blueprint("movimentacao", __name__, url_prefix="/movimentacoes")


@mov_bp.route("/saida", methods=["POST"])
@login_required
def registrar_saida_route():
    veiculo_id = request.form.get("veiculo_id", type=int)
    km_saida = request.form.get("km_saida", type=int)

    if not veiculo_id or km_saida is None:
        flash("É obrigatório informar o veículo e a KM de saída.", "danger")
        return redirect(url_for("main.home"))

    try:
        registrar_saida_service(veiculo_id=veiculo_id, km_saida=km_saida, operador_id=current_user.id)
        flash("Saída registrada com sucesso!", "success")
    except RegraNegocioError as e:
        flash(str(e), "warning")

    return redirect(url_for("main.home"))


@mov_bp.route("/retorno/<int:id>", methods=["POST"])
@login_required
def registrar_retorno_route(id):
    km_retorno = request.form.get("km_retorno", type=int)

    if km_retorno is None:
        flash("É obrigatório informar a KM de retorno.", "danger")
        return redirect(url_for("main.home"))

    try:
        registrar_retorno_service(mov_id=id, km_retorno=km_retorno, operador_id=current_user.id)
        flash("Retorno registrado com sucesso!", "success")
    except RegraNegocioError as e:
        flash(str(e), "warning")

    return redirect(url_for("main.home"))