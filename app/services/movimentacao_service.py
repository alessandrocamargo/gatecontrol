from datetime import datetime
from flask import current_app
from flask_login import current_user
from app.extensions import db
from app.models.veiculo import Veiculo,STATUS_DISPONIVEL, STATUS_EM_USO
from app.models.movimentacao_veiculo import MovimentacaoVeiculo

class RegraNegocioError(Exception):
    """Erro de regra de negócio (retorna 400 nas rotas)"""
    pass

def registrar_saida(veiculo_id: int, km_saida: int) -> MovimentacaoVeiculo:
    veiculo = Veiculo.query.get_or_404(veiculo_id)

    if veiculo.status != STATUS_DISPONIVEL:
        raise RegraNegocioError("Veiculo não está disponivel para saida.")
    
    if km_saida is None:
        raise RegraNegocioError("É necessário informar a KM de saida.")
    
    # Cria a movimetação aberta
    mov = MovimentacaoVeiculo(
        veiculo_id = veiculo.id,
        km_saida = km_saida,
        data_saida = datetime.utcnow(),
        status = STATUS_EM_USO,
        operador_saida_id = current_user.id
    )

    veiculo.status = STATUS_EM_USO

    db.session.add(mov)
    db.session.commit()
    return mov

def registrar_retorno(movimentacao_id: int, km_retorno: int) -> MovimentacaoVeiculo:
    mov = MovimentacaoVeiculo.query.get_or_404(movimentacao_id)

    if mov.status != STATUS_EM_USO:
        raise RegraNegocioError("Movimentação já está finalizada u inválida")
    
    if km_retorno is None:
        raise RegraNegocioError("É necessário informar a KM de retorno")
    
    if mov.km_saida is not None and km_retorno < mov.saida:
        raise RegraNegocioError("Km de retorno não pode ser menor que Km de saída.")
    
    mov.km_retorno = km_retorno
    mov.data_retorno = datetime.utcnow()
    mov.status = STATUS_DISPONIVEL
    mov.operador_retorno_id = current_user.id

    # Atualiza veículo
    Veiculo = Veiculo.query.get(mov.veiculo_id)
    if Veiculo:
        Veiculo.status = STATUS_DISPONIVEL
        db.session.commit()
        return mov
    