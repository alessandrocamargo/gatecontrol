from .. import db
from datetime import datetime

# Constantes (recomendado)
STATUS_DISPONIVEL = "disponivel"
STATUS_EM_USO = "em_uso"


class Veiculo(db.Model):
    __tablename__ = "veiculos"

    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(10), nullable=False, unique=True)
    modelo = db.Column(db.String(100), nullable=False)

    # FK
    setor_id = db.Column(db.Integer, db.ForeignKey("setores.id"), nullable=False)

    # ✅ status mais claro para o operador
    status = db.Column(db.String(20), nullable=False, default=STATUS_DISPONIVEL)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamento (ajuste se seu nome estiver diferente)
    setor = db.relationship("Setor", backref="veiculos")

    def __repr__(self):
        return f"<Veiculo {self.placa} ({self.status})>"