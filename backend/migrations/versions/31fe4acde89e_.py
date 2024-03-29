"""empty message

Revision ID: 31fe4acde89e
Revises: 
Create Date: 2021-03-03 20:00:43.615516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31fe4acde89e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('acao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticker', sa.String(length=64), nullable=True),
    sa.Column('dy', sa.Integer(), nullable=True),
    sa.Column('patr_liq', sa.BigInteger(), nullable=True),
    sa.Column('roe', sa.Integer(), nullable=True),
    sa.Column('vpa', sa.Integer(), nullable=True),
    sa.Column('lpa', sa.Integer(), nullable=True),
    sa.Column('n_acoes', sa.BigInteger(), nullable=True),
    sa.Column('lucro_liq', sa.BigInteger(), nullable=True),
    sa.Column('payout', sa.Integer(), nullable=True),
    sa.Column('margem_liq', sa.Integer(), nullable=True),
    sa.Column('cres5', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_acao_ticker'), 'acao', ['ticker'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_acao_ticker'), table_name='acao')
    op.drop_table('acao')
    # ### end Alembic commands ###
