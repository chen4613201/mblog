"""empty message

Revision ID: dd0b0f3267f8
Revises: 
Create Date: 2020-05-13 11:34:30.402608

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dd0b0f3267f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Users')
    op.drop_table('download__record')
    op.drop_table('Article')
    op.add_column('C_T__article', sa.Column('article_attr', sa.String(length=64), nullable=True))
    op.add_column('C_T__article', sa.Column('article_title', sa.String(length=128), nullable=True))
    op.drop_column('C_T__article', 'artircle_title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('C_T__article', sa.Column('artircle_title', mysql.VARCHAR(length=128), nullable=True))
    op.drop_column('C_T__article', 'article_title')
    op.drop_column('C_T__article', 'article_attr')
    op.create_table('Article',
    sa.Column('articleid', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('content', mysql.MEDIUMTEXT(), nullable=True),
    sa.Column('thumbs', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('read', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('message', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('create_time', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('articleid'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('download__record',
    sa.Column('Id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('User_Email', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('Veri_Code', mysql.VARCHAR(length=24), nullable=True),
    sa.PrimaryKeyConstraint('Id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('Users',
    sa.Column('userid', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('create_time', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('userid'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###