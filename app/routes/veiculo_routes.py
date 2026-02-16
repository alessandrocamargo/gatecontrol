from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.veiculo import Veiculo
from app.models.setor import Setor
from app.extensions import db

veiculo_bp = Blueprint("veiculo", __name__, url_prefix="/veiculos")


# 🔹 LISTAR VEÍCULOS
@veiculo_bp.route("/")
# @login_required
def listar_veiculos():
    veiculos = Veiculo.query.order_by(Veiculo.id.desc()).all()
    return render_template("veiculo_list.html", veiculos=veiculos)


# 🔹 CRIAR VEÍCULO
@veiculo_bp.route("/criar", methods=["GET", "POST"])
# @login_required
def criar_veiculo():
    setores = Setor.query.all()

    if request.method == "POST":
        placa = request.form.get("placa")
        modelo = request.form.get("modelo")
        setor_id = request.form.get("setor_id")

        if not placa or not modelo or not setor_id:
            flash("Todos os campos são obrigatórios.", "error")
            return redirect(url_for("veiculo.criar_veiculo"))

        veiculo_existente = Veiculo.query.filter_by(placa=placa).first()
        if veiculo_existente:
            flash("Já existe um veículo com essa placa.", "error")
            return redirect(url_for("veiculo.criar_veiculo"))

        novo_veiculo = Veiculo(
            placa=placa.upper(),
            modelo=modelo,
            setor_id=setor_id
        )

        db.session.add(novo_veiculo)
        db.session.commit()

        flash("Veículo cadastrado com sucesso!", "success")
        return redirect(url_for("veiculo.listar_veiculos"))

    return render_template("veiculo_form.html", setores=setores)
