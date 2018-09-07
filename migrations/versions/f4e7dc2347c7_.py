"""empty message

Revision ID: f4e7dc2347c7
Revises: 7bcf6200209d
Create Date: 2018-09-07 11:59:44.046135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4e7dc2347c7'
down_revision = '7bcf6200209d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'type',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.drop_index('ix_users_type', table_name='users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_users_type', 'users', ['type'], unique=False)
    op.alter_column('users', 'type',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###
