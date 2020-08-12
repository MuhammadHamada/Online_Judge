"""empty message

Revision ID: a0624d6b10a2
Revises: 715de3dadd1b
Create Date: 2020-08-12 15:30:08.713719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0624d6b10a2'
down_revision = '715de3dadd1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Solution')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Solution',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Solution_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('verdict', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('problem_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('code', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['problem_id'], ['Problem.id'], name='Solution_problem_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], name='Solution_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='Solution_pkey')
    )
    # ### end Alembic commands ###