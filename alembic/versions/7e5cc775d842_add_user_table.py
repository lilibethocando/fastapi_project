"""add user table

Revision ID: 7e5cc775d842
Revises: 9f2dca2da973
Create Date: 2022-03-24 04:40:38.552866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e5cc775d842'
down_revision = '9f2dca2da973'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created at', sa.TIMESTAMP(timezone=True),
              server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )


def downgrade():
    op.drop_table('users')
