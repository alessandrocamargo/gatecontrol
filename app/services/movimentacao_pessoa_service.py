from datetime import datetime
from app.extensions import db
from app.models.pessoa import Pessoa
from app.models.movimentacao_pessoa import MovimentacaoPessoa, STATUS_DENTRO, STATUS_SAIU

class RegraNegocioError(Exception):
    """Erro usado quando alguma regra de negocio da portaria é violada"""
    pass

# ==========================
# REGISTRAR ENTRADA
# ==========================
def registrar_entrada_pessoa(*, pessoa_id:int, operador_id: int) -> MovimentacaoPessoa:
    pessoa = Pessoa.query.get_or_404(pessoa_id)

    # 🔒 Regra: pessoa não pode entrar duas vezes sem sair
    movimentacao_aberta = MovimentacaoPessoa.query.filter_by(
        pessoa_id = pessoa.id,
        status = STATUS_DENTRO
    ).first

    if movimentacao_aberta:
        raise RegraNegocioError("Está pessoa já entrou")
    
    mov = MovimentacaoPessoa(
        pessoa_id = pessoa.id,
        operador_entrada_id = operador_id,
        data_entrada = datetime.utcnow(),
        status = STATUS_DENTRO
    )

    db.session.add(mov)
    db.session.commit()
    return mov

# ================
# REGISTRAR SAIDA
# ================
def registrar_saida_pessoa(*, mov_id:int, operador_id:int) -> MovimentacaoPessoa:
    mov = MovimentacaoPessoa.query.get_or_404(mov_id)

    #🔒 Regra: só pode sair se estiver dentro
    if mov.status != STATUS_DENTRO:
        raise RegraNegocioError("Esse visitante / prestador já saiu.")
    
    mov.data_saida = datetime.utcnow()
    mov.operador_saida_id = operador_id
    mov.status = STATUS_SAIU

    db.session.commit()

    return mov
