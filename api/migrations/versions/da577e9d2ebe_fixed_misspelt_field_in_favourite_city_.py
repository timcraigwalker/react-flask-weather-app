"""fixed misspelt field in favourite city table.

Revision ID: da577e9d2ebe
Revises: 5a1872c61897
Create Date: 2024-02-26 15:14:20.826179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da577e9d2ebe'
down_revision = '5a1872c61897'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_favourite_cities', schema=None) as batch_op:
        batch_op.add_column(sa.Column('longitude', sa.Float(precision=10), nullable=True))
        batch_op.drop_constraint('_user_favourite_city_uc', type_='unique')
        batch_op.create_unique_constraint('_user_favourite_city_uc', ['user_id', 'city', 'latitude', 'longitude'])
        batch_op.drop_column('longitide')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_favourite_cities', schema=None) as batch_op:
        batch_op.add_column(sa.Column('longitide', sa.FLOAT(), nullable=True))
        batch_op.drop_constraint('_user_favourite_city_uc', type_='unique')
        batch_op.create_unique_constraint('_user_favourite_city_uc', ['user_id', 'city', 'latitude', 'longitide'])
        batch_op.drop_column('longitude')

    # ### end Alembic commands ###
