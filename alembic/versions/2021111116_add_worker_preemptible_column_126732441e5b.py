"""add worker preemptible column

Revision ID: 126732441e5b
Revises: 26a5e6b3bfa5
Create Date: 2021-11-11 16:24:55.756149

"""

# revision identifiers, used by Alembic.
revision = '126732441e5b'
down_revision = '26a5e6b3bfa5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('worker', sa.Column('preemptible', sa.Boolean(), nullable=True))
    op.execute("UPDATE worker SET preemptible = false")
    op.alter_column('worker', 'worker', nullable=False)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('worker', 'preemptible')
    # ### end Alembic commands ###
