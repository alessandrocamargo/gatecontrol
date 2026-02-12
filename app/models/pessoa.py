from .. import db
from datetime import datetime
from sqlalchemy.orm import validates

class Pessoa(db.Model):
    __tablename__ = "pessoa"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    documento = db.Column(db.String(20), nullable=False, unique=True)
    tipo = db.Column(db.String(20), nullable=False) # visitante ou prestador

    @validates("tipo")
    def validar_tipo(self, key, tipo):
        if tipo not in ["visitante", "prestador"]:
            raise ValueError("Funcionários não podem ser cadastrados na portaria.")
        return tipo

    # Chave Estrangeira
    setor_id = db.Column(db.Integer, db.ForeignKey("setores.id"), nullable=False)

    # Relacionamento
    setor = db.relationship("Setor", backref="pessoa")

    def __repr__(self):
        return f"<Pessoa {self.nome} ({self.tipo})>"