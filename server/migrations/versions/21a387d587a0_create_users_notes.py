"""create users, notes

Revision ID: 21a387d587a0
Revises: 9305d89576ac
Create Date: 2023-02-19 13:11:47.111339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "21a387d587a0"
down_revision = "9305d89576ac"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("notes")
    op.drop_table("users")
    # ### end Alembic commands ###


# To avoid this issue, you can add a "revisions" flag
# to the "alembic upgrade" command to force Alembic to apply
# the migration script again, even if it has already been applied.
# This will update the "alembic_version" table to reflect that
# the migration script has been applied, and prevent Alembic from
# generating unnecessary SQL commands in the future.
# - what chatGPT had to say about this issue
# # # not tested yet # # #


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("username", sa.VARCHAR(length=80), nullable=False),
        sa.Column("password", sa.VARCHAR(length=128), nullable=False),
        sa.Column("created_at", sa.DATETIME(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "notes",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("title", sa.VARCHAR(length=255), nullable=False),
        sa.Column("content", sa.TEXT(), nullable=False),
        sa.Column("created_at", sa.DATETIME(), nullable=True),
        sa.Column("user_id", sa.INTEGER(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###
