"""minor

Revision ID: e68039eaa315
Revises: c2be595a5a01
Create Date: 2021-09-06 15:45:53.020740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e68039eaa315'
down_revision = 'c2be595a5a01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('passwords_password_key', 'passwords', type_='unique')
    op.create_unique_constraint(None, 'passwords', ['pid'])
    op.create_unique_constraint(None, 'users', ['uid'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'passwords', type_='unique')
    op.create_unique_constraint('passwords_password_key', 'passwords', ['password'])
    # ### end Alembic commands ###
