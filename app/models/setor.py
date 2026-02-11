from .. import db
from datetime import datetime

class Setor(db.Model):
    __tablename__ = "setores"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Serve para mostrar os dados em logos ou erros do bd
    def __repr__(self):
        return f"<Setor {self.nome}>"