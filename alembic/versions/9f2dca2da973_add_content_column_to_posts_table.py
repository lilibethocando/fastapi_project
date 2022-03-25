"""add content column to posts table

Revision ID: 9f2dca2da973
Revises: 3cd8e4afcbb9
Create Date: 2022-03-23 10:22:21.012924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f2dca2da973'
down_revision = '3cd8e4afcbb9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    


def downgrade():
    op.drop_column('posts', 'content')
