"""First migration by models

Revision ID: 2e5acf076c84
Revises: 
Create Date: 2024-02-13 10:03:56.531252

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2e5acf076c84'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('perval_areas',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('id_parent', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pereval_areas')
    op.alter_column('images', 'img',
               existing_type=postgresql.BYTEA(),
               nullable=True)
    op.add_column('pereval_added', sa.Column('beauty_title', sa.String(), nullable=True))
    op.add_column('pereval_added', sa.Column('other_titles', sa.String(), nullable=True))
    op.alter_column('pereval_added', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('pereval_id_seq'::regclass)"))
    op.drop_column('pereval_added', 'beautytitle')
    op.drop_column('pereval_added', 'other_title')
    op.alter_column('spr_activities_types', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('untitled_table_200_id_seq'::regclass)"))
    op.alter_column('spr_activities_types', 'title',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=True)
    op.alter_column('users', 'fam',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=True)
    op.alter_column('users', 'name',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=True)
    op.alter_column('users', 'otc',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=True)
    op.alter_column('users', 'email',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'email',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=False)
    op.alter_column('users', 'otc',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.alter_column('users', 'name',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.alter_column('users', 'fam',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.alter_column('spr_activities_types', 'title',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.alter_column('spr_activities_types', 'id',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('untitled_table_200_id_seq'::regclass)"))
    op.add_column('pereval_added', sa.Column('other_title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('pereval_added', sa.Column('beautytitle', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.alter_column('pereval_added', 'id',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('pereval_id_seq'::regclass)"))
    op.drop_column('pereval_added', 'other_titles')
    op.drop_column('pereval_added', 'beauty_title')
    op.alter_column('images', 'img',
               existing_type=postgresql.BYTEA(),
               nullable=False)
    op.create_table('pereval_areas',
    sa.Column('id', sa.BIGINT(), server_default=sa.text("nextval('pereval_areas_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('id_parent', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('title', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='pereval_areas_pkey')
    )
    op.drop_table('perval_areas')
    # ### end Alembic commands ###
