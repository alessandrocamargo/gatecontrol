from .. import db
from datetime import datetime

class Veiculo(db.Model):
    __tablename__ = "veiculos"

    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(10), unique=True, nullable=False)
    modelo = db.Column(db.String(100))

    setor_id = db.Column(db.Integer, db.ForeignKey("setores.id"), nullable=False)
    setor = db.relationship("Setor", backref="veiculos")

    def __repr__(self):
        return f"<Veiculo {self.placa}>"
