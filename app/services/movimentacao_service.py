from datetime import datetime

from app.extensions import db
from app.models.veiculo import Veiculo, STATUS_EM_USO, STATUS_DISPONIVEL
from app.models.movimentacao_veiculo import MovimentacaoVeiculo


class RegraNegocioError(Exception):
    pass


def registrar_saida_service(*, veiculo_id: int, km_saida: int, operador_id: int) -> MovimentacaoVeiculo:
    veiculo = Veiculo.query.get_or_404(veiculo_id)

    if km_saida is None:
        raise RegraNegocioError("Informe a KM de saída.")
    if km_saida < 0:
        raise RegraNegocioError("KM de saída não pode ser negativa.")

    mov_aberta = MovimentacaoVeiculo.query.filter_by(
        veiculo_id=veiculo_id,
        status=STATUS_EM_USO
    ).first()

    if mov_aberta or veiculo.status == STATUS_EM_USO:
        raise RegraNegocioError("Esse veículo já está em uso (há uma movimentação aberta).")

    mov = MovimentacaoVeiculo(
        veiculo_id=veiculo_id,
        km_saida=km_saida,
        operador_saida_id=operador_id,
        data_saida=datetime.utcnow(),
        status=STATUS_EM_USO,
    )

    veiculo.status = STATUS_EM_USO

    db.session.add(mov)
    db.session.commit()
    return mov


def registrar_retorno_service(*, mov_id: int, km_retorno: int, operador_id: int) -> MovimentacaoVeiculo:
    mov = MovimentacaoVeiculo.query.get_or_404(mov_id)

    if mov.status != STATUS_EM_USO:
        raise RegraNegocioError("Essa movimentação já foi finalizada.")

    if km_retorno is None:
        raise RegraNegocioError("Informe a KM de retorno.")
    if km_retorno < mov.km_saida:
        raise RegraNegocioError("KM de retorno não pode ser menor que a KM de saída.")

    mov.km_retorno = km_retorno
    mov.data_retorno = datetime.now()
    mov.operador_retorno_id = operador_id
    mov.status = "finalizado"

    if mov.veiculo:
        mov.veiculo.status = STATUS_DISPONIVEL

    db.session.commit()
    return mov