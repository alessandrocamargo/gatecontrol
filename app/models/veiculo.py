from .. import db
from datetime import datetime

class Veiculo(db.Model):
    __tablename__ = "veiculos"

    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(10), nullable=False, unique=True)
    modelo = db.Column(db.String(100), nullable=False)

    # ForeignKey correta (porque tabela é "setores")
    setor_id = db.Column(db.Integer, db.ForeignKey("setores.id"), nullable=False)

    status = db.Column(db.String(10), nullable=False, default="fora")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship usa nome da CLASSE
    setor = db.relationship("Setor", backref="veiculos")

    def __repr__(self):
        return f"<Veiculo {self.placa}>"
