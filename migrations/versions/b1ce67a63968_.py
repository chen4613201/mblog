"""empty message

Revision ID: b1ce67a63968
Revises: dd0b0f3267f8
Create Date: 2020-05-13 11:39:42.082608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1ce67a63968'
down_revision = 'dd0b0f3267f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('C_T__article', sa.Column('cover_photo', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('C_T__article', 'cover_photo')
    # ### end Alembic commands ###
