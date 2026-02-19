from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.veiculo import Veiculo, STATUS_DISPONIVEL, STATUS_EM_USO
from app.models.movimentacao_veiculo import MovimentacaoVeiculo

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
@login_required
def home():
    veiculos = Veiculo.query.order_by(Veiculo.placa.asc()).all()

    # Movimentações abertas (em uso)
    abertas = MovimentacaoVeiculo.query.filter_by(status=STATUS_EM_USO).all()
    mov_aberta_por_veiculo = {m.veiculo_id: m.id for m in abertas}

    # Dashboard
    total = len(veiculos)
    disponiveis = sum(1 for v in veiculos if v.status == STATUS_DISPONIVEL)
    em_uso = sum(1 for v in veiculos if v.status == STATUS_EM_USO)

    return render_template(
        "home.html",
        user=current_user,   # <-- necessário se no html está {{ user.username }}
        veiculos=veiculos,
        total=total,
        disponiveis=disponiveis,
        em_uso=em_uso,
        mov_aberta_por_veiculo=mov_aberta_por_veiculo,
        STATUS_DISPONIVEL=STATUS_DISPONIVEL,
        STATUS_EM_USO=STATUS_EM_USO
    )
