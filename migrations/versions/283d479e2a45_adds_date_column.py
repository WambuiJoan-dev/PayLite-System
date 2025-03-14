"""adds date column

Revision ID: 283d479e2a45
Revises: 
Create Date: 2025-03-14 13:41:22.552832

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '283d479e2a45'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('payments', 'date_paid',
               existing_type=sa.INTEGER(),
               type_=sa.DateTime(),
               existing_nullable=True)
    op.alter_column('payments', 'next_due_date',
               existing_type=sa.INTEGER(),
               type_=sa.DateTime(),
               existing_nullable=True)
    op.alter_column('payments', 'sale_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('payments', 'sale_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('payments', 'next_due_date',
               existing_type=sa.DateTime(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.alter_column('payments', 'date_paid',
               existing_type=sa.DateTime(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    # ### end Alembic commands ###
