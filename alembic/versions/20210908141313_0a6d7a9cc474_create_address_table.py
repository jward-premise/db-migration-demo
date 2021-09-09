"""create address table

Revision ID: 0a6d7a9cc474
Revises: 08ebf4a91c1b
Create Date: 2021-09-08 14:13:13.693110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a6d7a9cc474'
down_revision = '08ebf4a91c1b'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute("""
        CREATE TABLE address
        (
            street_number INT NOT NULL,
            street_name TEXT NOT NULL,
            apt_num TEXT,
            city TEXT NOT NULL,
            state TEXT NOT NULL
        );
    """)


def downgrade():
    conn = op.get_bind()
    conn.execute("""
        DROP TABLE address;
    """)
