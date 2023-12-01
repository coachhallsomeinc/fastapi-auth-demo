"""empty message

Revision ID: 72fb7301a163
Revises: 12a2f017a55a
Create Date: 2023-11-22 04:29:21.785921

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '72fb7301a163'
down_revision: Union[str, None] = '12a2f017a55a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.String(), nullable=True))
    op.drop_index('ix_users_full_name', table_name='users')
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.drop_column('users', 'full_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('full_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.create_index('ix_users_full_name', 'users', ['full_name'], unique=False)
    op.drop_column('users', 'username')
    # ### end Alembic commands ###
