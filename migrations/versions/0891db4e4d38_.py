"""empty message

Revision ID: 0891db4e4d38
Revises: d8e63db00735
Create Date: 2022-10-24 15:57:20.584163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0891db4e4d38'
down_revision = 'd8e63db00735'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('items', 'price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('items', 'price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)
    # ### end Alembic commands ###
