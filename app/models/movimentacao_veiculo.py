from datetime import datetime
from .. import db

class MovimentacaoVeiculo(db.Model):
    __tablename__ = "movimentacoes_veiculo"

    id = db.Column(db.Integer, primary_key=True)

    veiculo_id = db.Column(db.Integer, db.ForeignKey("veiculos.id"), nullable=False)
    veiculo = db.relationship("Veiculo", backref="movimentacoes")

    operador_saida_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    operador_saida = db.relationship("User", foreign_keys=[operador_saida_id])

    operador_retorno_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    operador_retorno = db.relationship("User", foreign_keys=[operador_retorno_id])

    data_saida = db.Column(db.DateTime, default=datetime.utcnow)
    km_saida = db.Column(db.Integer, nullable=False)

    data_retorno = db.Column(db.DateTime)
    km_retorno = db.Column(db.Integer)

    status = db.Column(db.String(20), default="em_uso")
