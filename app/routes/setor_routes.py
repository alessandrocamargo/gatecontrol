from flask import Blueprint, request, jsonify, render_template
from .. import db
from app.models.setor import Setor

setor_bp = Blueprint("setor", __name__)

@login_required
@setor_bp.route("/setor/form")
def form_setor():
    return render_template("setor_form.html")

# =========================
# Criar Setor
# =========================
@setor_bp.route("/setor", methods=["POST"])
def criar_setor():
    dados = request.get_json() or {}

    nome = dados.get("nome")

    if not nome:
        return jsonify({"erro": "Nome do setor é obrigatório"}), 400

    if Setor.query.filter_by(nome=nome).first():
        return jsonify({"erro": "Setor já cadastrado"}), 400

    novo_setor = Setor(nome=nome)

    db.session.add(novo_setor)
    db.session.commit()

    return jsonify({
        "id": novo_setor.id,
        "nome": novo_setor.nome
    }), 201


# =========================
# Listar Setores
# =========================
@setor_bp.route("/setor", methods=["GET"])
def listar_setores():
    setores = Setor.query.all()

    resultado = []

    for s in setores:
        resultado.append({
            "id": s.id,
            "nome": s.nome
        })

    return jsonify(resultado), 200


# =========================
# Formulário HTML
# =========================
@setor_bp.route("/setor/form", methods=["GET"])
def form_setor():
    return render_template("setorForm.html")

# =========================
# PROTETOR DE ROTA
# =========================
from flask import login_required



