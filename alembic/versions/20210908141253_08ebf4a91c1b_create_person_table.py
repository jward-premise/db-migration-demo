"""create person table

Revision ID: 08ebf4a91c1b
Revises: e1a05cf5b0d3
Create Date: 2021-09-08 14:12:53.118496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08ebf4a91c1b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute("""
        CREATE TABLE person
        (
            first_name  TEXT    NOT NULL,
            last_name   TEXT    NOT NULL,
            age         INT     NOT NULL
        );
    """)


def downgrade():
    conn = op.get_bind()
    conn.execute("""
        DROP TABLE person;
    """)
