from flask import Blueprint, request, jsonify
from .. import db
from app.models.registro_entrada import RegistroEntrada
from app.models.pessoa import Pessoa
from app.models.veiculo import Veiculo
from datetime import datetime

registro_bp = Blueprint("registro", __name__)

@registro_bp.route("/entrada", methods=["POST"])
def registrar_entrada():
    data = request.json

    pessoa_id = data.get("pessoa_id")
    veiculo_id = data.get("veiculo_id")
    km_entrada = data.get("km_entrada")

    if not pessoa_id and not veiculo_id:
        return jsonify({"erro": "É necessário informar pessoa ou veiculo"})
    
    # Ser for veiculo, KM é obrigatorio
    if veiculo_id and not km_entrada:
        return jsonify({"erro:": "É necessário informar a KM quando for veiculo"}),400
    
    novo_registro = RegistroEntrada(
        pessoa_id = pessoa_id,
        veiculo_id = veiculo_id,
        km_entrada = km_entrada,
        data_entrada = datetime.utcnow()
    )

    db.session.add(novo_registro)
    db.session.commit()

    return jsonify({"mensagem" : "Entrada registrada com sucesso"}), 201

@registro_bp.route("/saida/<int:id>", methods=["PUT"])
def registrar_saida(id):
    registro = RegistroEntrada.query.get_or_404(id)

    if registro.data_saida:
        return jsonify({"erro": "Registro já finalizado"}), 400

    dados = request.get_json()

    # Se for veículo, validar KM
    if registro.veiculo:
        km_saida = dados.get("km_saida")

        if not km_saida:
            return jsonify({"erro": "É necessário informar KM na saída"}), 400

        if km_saida < registro.km_entrada:
            return jsonify({"erro": "KM saída não pode ser menor que KM entrada"}), 400

        registro.km_saida = km_saida
        registro.veiculo.status = "fora"

    registro.data_saida = datetime.utcnow()

    db.session.commit()

    return jsonify({"mensagem": "Saída registrada com sucesso"}), 200
