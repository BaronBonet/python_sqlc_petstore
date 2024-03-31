from sqlalchemy import Engine, text
import pytest

from adapters.postgres_repository.pet_store import PostgresPetStoreRepo


@pytest.fixture
def add_owner_and_pet(db_engine: Engine):
    with db_engine.connect() as connection:
        connection.execute(text(
            """
            INSERT INTO owners (name, email)
            VALUES 
                ('John Doe', 'john@example.com');
            INSERT INTO pets (id, name, species, breed, age, owner_id, created_at) VALUES (1, 'Fido', 'Dog', 'Labrador', 3, 1, now())
            """
        ))
        connection.commit()


def test_get_pet(db_engine, add_owner_and_pet):
    repo = PostgresPetStoreRepo(db_engine)
    with repo as r:
        pet = r.get_pet(1)
        assert pet is not None
        assert pet.id == 1
