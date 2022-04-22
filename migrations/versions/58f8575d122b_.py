"""empty message

Revision ID: 58f8575d122b
Revises: a33de1c2cb42
Create Date: 2022-04-22 16:52:59.462878

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '58f8575d122b'
down_revision = 'a33de1c2cb42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('wechat_user', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('wechat_user', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
