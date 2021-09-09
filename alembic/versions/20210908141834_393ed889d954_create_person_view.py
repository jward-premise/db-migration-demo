"""create person view

Revision ID: 393ed889d954
Revises: 0a6d7a9cc474
Create Date: 2021-09-08 14:18:34.297538

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '393ed889d954'
down_revision = '0a6d7a9cc474'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute("""
        DROP VIEW IF EXISTS person_read;
        CREATE VIEW person_read AS (
            SELECT 
                  first_name || ' ' || last_name as name
                , age
              FROM person
        );
    """)


def downgrade():
    conn = op.get_bind()
    conn.execute("""
        DROP VIEW IF EXISTS person_read;
    """)
