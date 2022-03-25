"""create posts table

Revision ID: 3cd8e4afcbb9
Revises: 
Create Date: 2022-03-23 09:58:00.055610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cd8e4afcbb9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable=False))


def downgrade():
    op.drop_table('posts')
    pass
