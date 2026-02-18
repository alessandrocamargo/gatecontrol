from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app.extensions import db
from app.models.veiculo import Veiculo, STATUS_DISPONIVEL, STATUS_EM_USO
from app.models.movimentacao_veiculo import MovimentacaoVeiculo

mov_bp = Blueprint("movimentacao", __name__, url_prefix="/movimentacoes")


# =========================
# SAÍDA - Form + Registro
# =========================
@mov_bp.route("/saida", methods=["GET", "POST"])
@login_required
def registrar_saida():
    veiculos = Veiculo.query.order_by(Veiculo.placa.asc()).all()

    # ✅ se vier da home: /movimentacoes/saida?veiculo_id=3
    veiculo_selecionado_id = request.args.get("veiculo_id", type=int)

    if request.method == "POST":
        veiculo_id = request.form.get("veiculo_id")
        km_saida = request.form.get("km_saida")

        if not veiculo_id or not km_saida:
            flash("Selecione um veículo e informe a KM de saída.", "error")
            return redirect(url_for("movimentacao.registrar_saida"))

        try:
            km_saida = int(km_saida)
        except ValueError:
            flash("KM de saída inválida.", "error")
            return redirect(url_for("movimentacao.registrar_saida"))

        veiculo = Veiculo.query.get_or_404(int(veiculo_id))

        # Regra: não permitir nova saída se já estiver em uso
        mov_aberta = MovimentacaoVeiculo.query.filter_by(
            veiculo_id=veiculo.id,
            status=STATUS_EM_USO
        ).first()

        if mov_aberta or veiculo.status == STATUS_EM_USO:
            flash("Este veículo já está em uso (há uma movimentação aberta).", "error")
            return redirect(url_for("movimentacao.registrar_saida"))

        nova_mov = MovimentacaoVeiculo(
            veiculo_id=veiculo.id,
            km_saida=km_saida,
            operador_saida_id=current_user.id,
            data_saida=datetime.utcnow(),
            status=STATUS_EM_USO
        )

        # ✅ muda o status do veículo
        veiculo.status = STATUS_EM_USO

        db.session.add(nova_mov)
        db.session.commit()

        flash("Saída registrada com sucesso!", "success")
        return redirect(url_for("main.home"))

    return render_template(
        "saida_form.html",
        veiculos=veiculos,
        veiculo_selecionado_id=veiculo_selecionado_id
    )


# =========================
# LISTA - Retornos Pendentes
# =========================
@mov_bp.route("/retorno", methods=["GET"])
@login_required
def listar_retorno():
    abertas = MovimentacaoVeiculo.query.filter_by(status=STATUS_EM_USO).order_by(
        MovimentacaoVeiculo.data_saida.desc()
    ).all()

    return render_template("retorno_list.html", movimentacoes=abertas)


# =========================
# RETORNO - Form + Finalizar
# =========================
@mov_bp.route("/retorno/<int:id>", methods=["GET", "POST"])
@login_required
def registrar_retorno(id):
    mov = MovimentacaoVeiculo.query.get_or_404(id)

    if mov.status != STATUS_EM_USO:
        flash("Esta movimentação já foi finalizada.", "error")
        return redirect(url_for("main.home"))

    if request.method == "POST":
        km_retorno = request.form.get("km_retorno")

        if not km_retorno:
            flash("Informe a KM de retorno.", "error")
            return redirect(request.url)

        try:
            km_retorno = int(km_retorno)
        except ValueError:
            flash("KM de retorno inválida.", "error")
            return redirect(request.url)

        if km_retorno < mov.km_saida:
            flash("KM retorno não pode ser menor que KM saída.", "error")
            return redirect(request.url)

        mov.km_retorno = km_retorno
        mov.data_retorno = datetime.utcnow()
        mov.operador_retorno_id = current_user.id
        mov.status = "finalizado"

        # ✅ volta para disponível
        if mov.veiculo:
            mov.veiculo.status = STATUS_DISPONIVEL

        db.session.commit()

        flash("Retorno registrado com sucesso!", "success")
        return redirect(url_for("main.home"))

    return render_template("retorno_form.html", mov=mov)
