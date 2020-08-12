"""empty message

Revision ID: dae372741365
Revises: 75cafc0f42dc
Create Date: 2020-08-12 14:10:33.560681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dae372741365'
down_revision = '75cafc0f42dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Contest_name_key', 'Contest', type_='unique')
    op.create_unique_constraint(None, 'User', ['handle'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'User', type_='unique')
    op.create_unique_constraint('Contest_name_key', 'Contest', ['name'])
    # ### end Alembic commands ###