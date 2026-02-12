from flask import Blueprint, request, jsonify, render_template
from app import db
from app.models.pessoa import Pessoa

pessoa_bp = Blueprint("pessoa", __name__)


# =========================
# Criar Pessoa
# =========================
@pessoa_bp.route("/pessoa", methods=["POST"])
def criar_pessoa():
    dados = request.get_json() or {}

    nome = dados.get("nome")
    documento = dados.get("documento")
    tipo = dados.get("tipo")
    setor_id = dados.get("setor_id")

    if not nome or not documento or not tipo or not setor_id:
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400

    if tipo not in ["visitante", "prestador"]:
        return jsonify({"erro": "Tipo deve ser visitante ou prestador"}), 400

    if Pessoa.query.filter_by(documento=documento).first():
        return jsonify({"erro": "Documento já cadastrado"}), 400

    nova_pessoa = Pessoa(
        nome=nome,
        documento=documento,
        tipo=tipo,
        setor_id=setor_id
    )

    db.session.add(nova_pessoa)
    db.session.commit()

    return jsonify({"mensagem": "Pessoa cadastrada com sucesso"}), 201


# =========================
# Listar Pessoas
# =========================
@pessoa_bp.route("/pessoa", methods=["GET"])
def listar_pessoas():
    pessoas = Pessoa.query.all()

    resultado = []

    for p in pessoas:
        resultado.append({
            "id": p.id,
            "nome": p.nome,
            "documento": p.documento,
            "tipo": p.tipo,
            "setor_id": p.setor_id
        })

    return jsonify(resultado), 200



# =========================
# FORMULARIO PESSOA
# =========================
@pessoa_bp.route("/pessoa/form", methods=["GET"])
def form_pessoa():
    return render_template("pessoaForm.html")
