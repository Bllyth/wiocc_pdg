"""empty message

Revision ID: 48a360167e8d
Revises: 
Create Date: 2021-09-15 08:13:32.939901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48a360167e8d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=1028), nullable=True),
    sa.Column('department', sa.String(length=1028), nullable=True),
    sa.Column('position', sa.String(length=1028), nullable=True),
    sa.Column('email', sa.String(length=1028), nullable=True),
    sa.Column('name', sa.String(length=1028), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('supervisor', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('oauth',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('provider', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('token', sa.JSON(), nullable=False),
    sa.Column('provider_user_id', sa.String(length=1028), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('provider_user_id')
    )
    op.create_table('pdg',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('supervisor_id', sa.Integer(), nullable=True),
    sa.Column('date_of_review', sa.String(), nullable=True),
    sa.Column('review_year', sa.String(), nullable=True),
    sa.Column('employee_feedback', sa.String(), nullable=True),
    sa.Column('supervisor_feedback', sa.String(), nullable=True),
    sa.Column('rating', sa.String(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['supervisor_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('next_year_objectives',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pdg_id', sa.Integer(), nullable=True),
    sa.Column('objective', sa.String(), nullable=True),
    sa.Column('measure_of_success', sa.String(), nullable=True),
    sa.Column('timeline', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['pdg_id'], ['pdg.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('objectives',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pdg_id', sa.Integer(), nullable=True),
    sa.Column('objective', sa.String(), nullable=True),
    sa.Column('measure_of_success', sa.String(), nullable=True),
    sa.Column('date_set', sa.DateTime(), nullable=True),
    sa.Column('timeline', sa.String(), nullable=True),
    sa.Column('self_evaluation', sa.String(), nullable=True),
    sa.Column('supervisor_evaluation', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['pdg_id'], ['pdg.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('training',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pdg_id', sa.Integer(), nullable=True),
    sa.Column('purpose', sa.String(), nullable=True),
    sa.Column('priority', sa.String(), nullable=True),
    sa.Column('target_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['pdg_id'], ['pdg.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('values',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pdg_id', sa.Integer(), nullable=True),
    sa.Column('client_focus', sa.String(), nullable=True),
    sa.Column('boundless', sa.String(), nullable=True),
    sa.Column('collaborate', sa.String(), nullable=True),
    sa.Column('integrity', sa.String(), nullable=True),
    sa.Column('personal_excellence', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['pdg_id'], ['pdg.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('values')
    op.drop_table('training')
    op.drop_table('objectives')
    op.drop_table('next_year_objectives')
    op.drop_table('pdg')
    op.drop_table('oauth')
    op.drop_table('users')
    op.drop_table('roles')
    # ### end Alembic commands ###
