from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.veiculo import Veiculo, STATUS_DISPONIVEL, STATUS_EM_USO
from app.models.movimentacao_veiculo import MovimentacaoVeiculo
from app.models.movimentacao_pessoa import MovimentacaoPessoa,STATUS_DENTRO
from app.models.setor import Setor

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
@login_required
def home():
    veiculos = Veiculo.query.order_by(Veiculo.placa.asc()).all()

    # Movimentações abertas (em uso)
    abertas = MovimentacaoVeiculo.query.filter_by(status=STATUS_EM_USO).all()
    mov_aberta_por_veiculo = {m.veiculo_id: m.id for m in abertas}

    pessoas_dentro = MovimentacaoPessoa.query.filter_by(status = STATUS_DENTRO).order_by(MovimentacaoPessoa.data_entrada.desc()).all()

    setor = Setor.query.order_by(Setor.nome.asc()).all()

    # Dashboard
    total = len(veiculos)
    disponiveis = sum(1 for v in veiculos if v.status == STATUS_DISPONIVEL)
    em_uso = sum(1 for v in veiculos if v.status == STATUS_EM_USO)

    visitantes = [
        m for m in pessoas_dentro
        if m.pessoa.tipo == "visitante"
    ]

    prestadores = [
        m for m in pessoas_dentro
        if m.pessoa.tipo == "prestador de serviço"
    ]

    transportadoras = [
        m for m in pessoas_dentro
        if m.pessoa.tipo == "transportadora"
    ]

    return render_template(
        "home.html",
        user=current_user,   # <-- necessário se no html está {{ user.username }}
        veiculos=veiculos,
        total=total,
        disponiveis=disponiveis,
        em_uso=em_uso,
        mov_aberta_por_veiculo=mov_aberta_por_veiculo,
        STATUS_DISPONIVEL=STATUS_DISPONIVEL,
        STATUS_EM_USO=STATUS_EM_USO,
        pessoas_dentro = pessoas_dentro,
        setores = setor,
        visitantes = visitantes,
        prestadores = prestadores,
        transportadoras = transportadoras
    )
