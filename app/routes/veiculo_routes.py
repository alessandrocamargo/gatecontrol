from flask import Blueprint, request, jsonify, render_template
from app import db
from app.models.veiculo import Veiculo

veiculo_bp = Blueprint("veiculo", __name__)


# =========================
# Criar Veículo
# =========================
@veiculo_bp.route("/veiculos", methods=["POST"])
def criar_veiculo():
    dados = request.get_json() or {}

    placa = dados.get("placa")
    modelo = dados.get("modelo")
    setor_id = dados.get("setor_id")

    if not placa or not modelo or not setor_id:
        return jsonify({"erro": "Placa, modelo e setor_id são obrigatórios"}), 400

    if Veiculo.query.filter_by(placa=placa).first():
        return jsonify({"erro": "Veículo já cadastrado com essa placa"}), 400

    novo_veiculo = Veiculo(
        placa=placa,
        modelo=modelo,
        setor_id=setor_id
    )

    db.session.add(novo_veiculo)
    db.session.commit()

    return jsonify({
        "id": novo_veiculo.id,
        "placa": novo_veiculo.placa,
        "modelo": novo_veiculo.modelo,
        "status": novo_veiculo.status
    }), 201


# =========================
# Listar Veículos
# =========================
@veiculo_bp.route("/veiculos", methods=["GET"])
def listar_veiculos():
    veiculos = Veiculo.query.all()

    resultado = []

    for v in veiculos:
        resultado.append({
            "id": v.id,
            "placa": v.placa,
            "modelo": v.modelo,
            "status": v.status,
            "setor_id": v.setor_id
        })

    return jsonify(resultado), 200


# =========================
# Buscar Veículo por ID
# =========================
@veiculo_bp.route("/veiculos/<int:id>", methods=["GET"])
def buscar_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)

    return jsonify({
        "id": veiculo.id,
        "placa": veiculo.placa,
        "modelo": veiculo.modelo,
        "status": veiculo.status,
        "setor_id": veiculo.setor_id
    }), 200


# =========================
# Atualizar Veículo
# =========================
@veiculo_bp.route("/veiculos/<int:id>", methods=["PUT"])
def atualizar_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)
    dados = request.get_json() or {}

    veiculo.placa = dados.get("placa", veiculo.placa)
    veiculo.modelo = dados.get("modelo", veiculo.modelo)

    db.session.commit()

    return jsonify({"mensagem": "Veículo atualizado com sucesso"}), 200


# =========================
# Deletar Veículo
# =========================
@veiculo_bp.route("/veiculos/<int:id>", methods=["DELETE"])
def deletar_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)

    db.session.delete(veiculo)
    db.session.commit()

    return jsonify({"mensagem": "Veículo deletado com sucesso"}), 200


# =========================
# FORMULARIO VEICULO
# =========================
@veiculo_bp.route("/veiculo/form", methods=["GET"])
def form_veiculo():
    return render_template("veiculoForm.html")