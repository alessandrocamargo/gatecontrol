from app import db
from datetime import datetime

class RegistroEntrada(db.Model):
    __tablename__ = "registros_entrada"
    id = db.Column(db.Interger, primary_key=True)

    # Chave Estrangeira
    pessoa_id = db.Column(db.Integer, db.ForeignKey("pessoas.id"), nullable=True)
    veiculo_id = db.Column(db.Integer, db.ForeignKey("veiculos.id"), nullable=True)


    # Relacionamento
    pessoa = db.relationship("Pessoa", backref="registros")
    veiculo = db.relationship("Veiculo", backref="registros")

    data_entrada = db.Column(db.DateTime, default=datetime.utcnow)
    data_saida = db.Column(db.DateTime, nullable=True)

    km_entrada = db.Column(db.Integer, nullable=True)
    km_saida = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"<RegistroEntrada {self.id} - Entrada {self.data_entrada}>"