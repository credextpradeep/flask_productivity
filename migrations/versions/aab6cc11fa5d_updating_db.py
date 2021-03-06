"""updating db

Revision ID: aab6cc11fa5d
Revises: 32c9f63da03b
Create Date: 2021-06-10 15:21:02.315973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aab6cc11fa5d'
down_revision = '32c9f63da03b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('organisation_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'organisations', ['organisation_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'organisation_id')
    # ### end Alembic commands ###
