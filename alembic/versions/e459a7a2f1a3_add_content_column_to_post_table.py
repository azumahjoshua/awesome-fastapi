"""add content column to post table

Revision ID: e459a7a2f1a3
Revises: bf4d3a36cdd9
Create Date: 2024-11-22 05:37:54.888913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e459a7a2f1a3'
down_revision: Union[str, None] = 'bf4d3a36cdd9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
