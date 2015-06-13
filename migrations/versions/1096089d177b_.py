"""empty message

Revision ID: 1096089d177b
Revises: 18d0d788f404
Create Date: 2015-06-13 15:40:50.128645

"""

# revision identifiers, used by Alembic.
revision = '1096089d177b'
down_revision = '18d0d788f404'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chats_to_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('chat_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['chat_id'], ['chats.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chats_to_users')
    ### end Alembic commands ###
