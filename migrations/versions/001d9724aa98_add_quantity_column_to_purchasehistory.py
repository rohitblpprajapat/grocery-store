"""Add quantity column to PurchaseHistory

Revision ID: 001d9724aa98
Revises: 73fe53a55809
Create Date: 2023-08-08 14:37:38.509337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001d9724aa98'
down_revision = '73fe53a55809'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchase_history', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quantity', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchase_history', schema=None) as batch_op:
        batch_op.drop_column('quantity')

    # ### end Alembic commands ###
