"""update veiculo status disponivel

Revision ID: 26c91841a271
Revises: 935c1278e865
Create Date: 2026-02-18 13:52:17.796617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26c91841a271'
down_revision = '935c1278e865'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("veiculos", schema=None) as batch_op:
        # adiciona created_at (ok ser nullable em tabela já existente)
        batch_op.add_column(sa.Column("created_at", sa.DateTime(), nullable=True))

        # garante modelo NOT NULL (se já tem dados, isso só funciona se não houver NULL)
        batch_op.alter_column(
            "modelo",
            existing_type=sa.VARCHAR(length=100),
            nullable=False
        )

        # ✅ adiciona status NOT NULL com server_default pra não quebrar no SQLite
        batch_op.add_column(
            sa.Column("status", sa.String(length=20), nullable=False, server_default="disponivel")
        )


def downgrade():
    with op.batch_alter_table("veiculos", schema=None) as batch_op:
        batch_op.alter_column(
            "modelo",
            existing_type=sa.VARCHAR(length=100),
            nullable=True
        )
        batch_op.drop_column("created_at")
        batch_op.drop_column("status")


    # ### end Alembic commands ###
