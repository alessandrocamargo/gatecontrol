from .. import db
from datetime import datetime

class RegistroEntrada(db.Model):
    __tablename__ = "registros_entrada"

    id = db.Column(db.Integer, primary_key=True)

    pessoa_id = db.Column(db.Integer, db.ForeignKey("pessoa.id"), nullable=True)
    veiculo_id = db.Column(db.Integer, db.ForeignKey("veiculos.id"), nullable=True)

    km_entrada = db.Column(db.Integer)
    km_saida = db.Column(db.Integer)

    data_entrada = db.Column(db.DateTime, default=datetime.utcnow)
    data_saida = db.Column(db.DateTime)

    pessoa = db.relationship("Pessoa", backref="registros")
    veiculo = db.relationship("Veiculo", backref="registros")

    


    def __repr__(self):
        return f"<RegistroEntrada {self.id} - Entrada {self.data_entrada}>"