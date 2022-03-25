"""add foreign-key to posts table

Revision ID: d166b72acc17
Revises: 7e5cc775d842
Create Date: 2022-03-24 04:55:44.868140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd166b72acc17'
down_revision = '7e5cc775d842'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
    local_cols=['user_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'user_id')
