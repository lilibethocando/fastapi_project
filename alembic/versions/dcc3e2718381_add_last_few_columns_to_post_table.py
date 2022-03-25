"""add last few columns to post table

Revision ID: dcc3e2718381
Revises: d166b72acc17
Create Date: 2022-03-24 05:08:38.584162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcc3e2718381'
down_revision = 'd166b72acc17'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),nullable=False, server_default=sa.text('NOW()')),)


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
