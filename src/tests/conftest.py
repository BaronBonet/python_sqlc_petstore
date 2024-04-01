import pathlib

import pytest
from sqlalchemy import Engine, create_engine, text
from testcontainers.postgres import PostgresContainer

MIGRATIONS_DIR = pathlib.Path(__file__).parent.parent.parent / "flyway" / "migrations"


def create_init_script(migrations_dir: pathlib.Path = MIGRATIONS_DIR) -> str:
    migration_text = ""
    migration_files = sorted(migrations_dir.glob("*.sql"))
    for migration_file in migration_files:
        with migration_file.open("r") as f:
            migration_text += f.read()
    return migration_text


@pytest.fixture(scope="session")
def db_engine():
    with PostgresContainer("postgres:15.6") as postgres:
        connection_url = postgres.get_connection_url()
        engine = create_engine(connection_url)

        run_migrations(engine)

        yield engine


@pytest.fixture(scope="function", autouse=True)
def cleanup_db(db_engine: Engine):
    yield

    with db_engine.begin() as connection:
        # Disable foreign key checks
        connection.execute(text("SET session_replication_role = 'replica'"))

        # Get the list of tables in the database
        result = connection.execute(
            text("SELECT tablename FROM pg_tables WHERE schemaname = 'public'")
        )
        tables = [row[0] for row in result]

        # Truncate all the tables
        for table in tables:
            connection.execute(text(f"TRUNCATE TABLE {table} CASCADE"))

        # Enable foreign key checks again
        connection.execute(text("SET session_replication_role = 'origin'"))


def run_migrations(db_engine: Engine):
    migration_text = create_init_script()
    with db_engine.connect() as connection:
        connection.execute(text(migration_text))
        connection.commit()
