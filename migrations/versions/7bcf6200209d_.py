"""empty message

Revision ID: 7bcf6200209d
Revises: 781445fc4978
Create Date: 2018-09-07 00:20:54.205330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bcf6200209d'
down_revision = '781445fc4978'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('type', sa.String(length=120), nullable=True))
    op.create_index(op.f('ix_users_type'), 'users', ['type'], unique=False)
    op.drop_index('ix_users_user_type', table_name='users')
    op.drop_column('users', 'user_type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_type', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.create_index('ix_users_user_type', 'users', ['user_type'], unique=False)
    op.drop_index(op.f('ix_users_type'), table_name='users')
    op.drop_column('users', 'type')
    # ### end Alembic commands ###
