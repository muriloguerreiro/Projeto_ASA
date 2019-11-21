"""empty message

Revision ID: 8d41e11f05f7
Revises: 1d7d56f9be79
Create Date: 2019-11-21 02:28:00.023760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d41e11f05f7'
down_revision = '1d7d56f9be79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('perfis', sa.Column('disc_1', sa.String(), nullable=True))
    op.add_column('perfis', sa.Column('disc_2', sa.String(), nullable=True))
    op.add_column('perfis', sa.Column('disc_3', sa.String(), nullable=True))
    op.add_column('perfis', sa.Column('disc_4', sa.String(), nullable=True))
    op.drop_column('perfis', 'disciplina_3')
    op.drop_column('perfis', 'disciplina_2')
    op.drop_column('perfis', 'disciplina_4')
    op.drop_column('perfis', 'disciplina_1')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('perfis', sa.Column('disciplina_1', sa.VARCHAR(), nullable=True))
    op.add_column('perfis', sa.Column('disciplina_4', sa.VARCHAR(), nullable=True))
    op.add_column('perfis', sa.Column('disciplina_2', sa.VARCHAR(), nullable=True))
    op.add_column('perfis', sa.Column('disciplina_3', sa.VARCHAR(), nullable=True))
    op.drop_column('perfis', 'disc_4')
    op.drop_column('perfis', 'disc_3')
    op.drop_column('perfis', 'disc_2')
    op.drop_column('perfis', 'disc_1')
    # ### end Alembic commands ###
