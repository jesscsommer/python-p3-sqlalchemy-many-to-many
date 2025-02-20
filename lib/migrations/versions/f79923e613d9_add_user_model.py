"""Add User model

Revision ID: f79923e613d9
Revises: c85043d75768
Create Date: 2023-06-12 15:57:42.009675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f79923e613d9'
down_revision = 'c85043d75768'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game_users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game_users',
    sa.Column('game_id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name='fk_game_users_game_id_games'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_game_users_user_id_users'),
    sa.PrimaryKeyConstraint('game_id', 'user_id')
    )
    # ### end Alembic commands ###
