"""empty message

Revision ID: 2d6721adecef
Revises: 344a86a70a9a
Create Date: 2021-11-26 01:30:19.469065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d6721adecef'
down_revision = '344a86a70a9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('anime', sa.Column('media_type', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('anime', 'media_type')
    # ### end Alembic commands ###
