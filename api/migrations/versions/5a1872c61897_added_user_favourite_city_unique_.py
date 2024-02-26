"""added user favourite city unique constraint.

Revision ID: 5a1872c61897
Revises: 555a213b3b5d
Create Date: 2024-02-26 13:50:24.596726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a1872c61897'
down_revision = '555a213b3b5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_favourite_cities', schema=None) as batch_op:
        batch_op.create_unique_constraint('_user_favourite_city_uc', ['user_id', 'city', 'latitude', 'longitide'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_favourite_cities', schema=None) as batch_op:
        batch_op.drop_constraint('_user_favourite_city_uc', type_='unique')

    # ### end Alembic commands ###