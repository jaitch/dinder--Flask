"""empty message

Revision ID: 425e96743bda
Revises: 7eadfbcd3786
Create Date: 2020-01-02 21:15:22.114421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '425e96743bda'
down_revision = '7eadfbcd3786'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipe_ingredients',
    sa.Column('ingredient_id', sa.Integer(), nullable=True),
    sa.Column('recipe_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.id'], ),
    sa.ForeignKeyConstraint(['recipe_id'], ['raw_data.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipe_ingredients')
    # ### end Alembic commands ###
