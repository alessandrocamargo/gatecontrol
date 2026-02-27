from datetime import datetime
from app.extensions import db

# Status possiveis
STATUS_DENTRO = "dentro"
STATUS_SAIU = "saiu"

class MovimentacaoPessoa(db.Model):
    __tablename__ = "movimentacoes_pessoa"

    
    pessoa_id = db.Column(db.Interger, db.ForeignKey("pessoa.id"), nullable=False)

    operador_entrada_id = db.Column(db.Interger, db.ForeignKey("user.id"), nullable=False)
    operador_saida_id = db.Column(db.Interger, db.ForeignKey("user.id"), nullable=False)

    data_entrada = db.Column(db.DateTime, nullable= False, default= datetime.utcnow)
    data_saida = db.Column(db.DataTime, nullable= False, default= datetime.utcnow)

    status = db.Column(db.String(20), nullable= False,default= STATUS_DENTRO)

    # =========================
    # RELACIONAMENTOS
    # =========================

    pessoa = db.relationship("Pessoa",backref="movimentacoes")
    operador_entrada = db.relationship("User", foreign_keys=[operador_entrada_id])
    operador_saida = db.relationship("User", foreign_keys=[operador_saida_id])

    def __repr__(self):
        return f"<MovimentacaoPessoa{self.id} pessoa={self.pessoa_id} status={self.status}>"