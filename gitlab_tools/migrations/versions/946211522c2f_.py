"""Add periodic_sync column to support periodic syncs

Revision ID: 946211522c2f
Revises: cad4d8aacceb
Create Date: 2018-06-08 12:44:28.966293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '946211522c2f'
down_revision = 'cad4d8aacceb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pull_mirror', sa.Column('periodic_sync', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('push_mirror', 'periodic_sync')
    # ### end Alembic commands ###
