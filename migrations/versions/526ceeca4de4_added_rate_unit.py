"""added rate/unit

Revision ID: 526ceeca4de4
Revises: 25a49b8fb830
Create Date: 2023-08-10 16:52:29.724224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '526ceeca4de4'
down_revision = '25a49b8fb830'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('rate',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('rate',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###