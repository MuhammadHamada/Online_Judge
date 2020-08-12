"""empty message

Revision ID: 75cafc0f42dc
Revises: 79cd020f3056
Create Date: 2020-08-12 14:07:42.222082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75cafc0f42dc'
down_revision = '79cd020f3056'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Contest', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Contest', type_='unique')
    # ### end Alembic commands ###
