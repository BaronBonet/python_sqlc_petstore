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
        print(connection_url)
        engine = create_engine(connection_url)

        run_migrations(engine)

        yield engine


def run_migrations(db_engine: Engine):
    migration_text = create_init_script()
    with db_engine.connect() as connection:
        connection.execute(text(migration_text))
        connection.commit()
