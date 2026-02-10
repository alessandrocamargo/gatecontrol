from app import db
from datetime import datetime

class Pessoa(db.Model):
    __tablename__ = "pessoa"

    id = db.Column(db.Interger, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    documento = db.Column(db.String(20), nullable=False, unique=True)
    tipo = db.Column(db.String(20), nullable=False) # visitante ou prestador

    # Chave Estrangeira
    setor_id = db.Column(db.Interger, db.Foreignkey("setores.id"), nullable=False)

    # Relacionamento
    setor = db.relationship("Setor", backref="pessoa")

    def __repr__(self):
        return f"<Pessoa {self.nome} ({self.tipo})>"