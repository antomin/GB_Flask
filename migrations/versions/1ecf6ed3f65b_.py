"""empty message

Revision ID: 1ecf6ed3f65b
Revises: d79f9428e6fa
Create Date: 2023-03-21 14:16:53.848361

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '1ecf6ed3f65b'
down_revision = 'd79f9428e6fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag')
    # ### end Alembic commands ###