"""empty message

Revision ID: 79cd020f3056
Revises: 36b2baab048e
Create Date: 2020-08-12 02:55:05.221392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79cd020f3056'
down_revision = '36b2baab048e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Solution', sa.Column('code', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Solution', 'code')
    # ### end Alembic commands ###