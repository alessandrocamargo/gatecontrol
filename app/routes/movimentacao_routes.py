from flask import Blueprint, request,jsonify
from flask_login import login_required
from app.services.movimentacao_service import (
    registrar_saida as srv_registrar_saida,
    registrar_retorno as srv_registrar_retorno,
    RegraNegocioError
)

movimentacao_bp = Blueprint("movimentacao", __name__, url_prefix="/movimentacao")

@movimentacao_bp.route("/saida", methods=["POST"])
@login_required
def saida():
    dados = request.get_json() or {}
    try:
        mov = srv_registrar_saida(
            veiculo_id = dados.get("veiculo_id"),
            km_saida = dados.get("km_saida")
        )
        return jsonify({"mensagem": "Saída registrada", "movimentacao_id" : mov.id}),201
    except RegraNegocioError as e:
        return jsonify({"erro": str(e)}),400
    
@movimentacao_bp.route("/retorno/<int:id>", methods=["PUT"])
@login_required
def retorno():
    dados = request.get_json or {}
    try:
        mov = srv_registrar_retorno(
            movimentacao_id = id,
            km_retorno =  dados.get("km_retorno")
        )
        return jsonify({"mensagem": "Retorno registrado", "movimentacao_id" : mov.id}),200
    except RegraNegocioError as e:
        return jsonify({"erro": str(e)}),400