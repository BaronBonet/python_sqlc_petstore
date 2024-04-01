from datetime import datetime

import pytest

from adapters.postgres_repository.pet_store import PostgresPetStoreRepo
from core import domain
from tests.helpers import TEST_DATA_DIR, TestData, add_test_data

id = 1
owner_stringer = TestData(
    template=TEST_DATA_DIR / "owners.sql",
    params=[{"name": "Stringer Bell", "email": "string@westside.com"}],
)
pet_fido = TestData(
    template=TEST_DATA_DIR / "pets.sql",
    params=[
        {
            "id": id,
            "name": "Fido",
            "species": "Dog",
            "breed": "Labrador",
            "age": 3,
            "owner_id": 1,
            "created_at": datetime(2023, 3, 31, 10, 0, 0),
        }
    ],
)


@pytest.mark.parametrize(
    "setup_data,result",
    [
        pytest.param(
            [
                owner_stringer,
                pet_fido,
            ],
            domain.Pet(
                id=id,
                name="Fido",
                species="Dog",
                breed="Labrador",
                age=3,
                owner_id=1,
                created_at=datetime(2023, 3, 31, 10, 0, 0),
            ),
            id="happy path",
        ),
        pytest.param(
            [
                owner_stringer,
            ],
            None,
            id="pet not found",
        ),
    ],
)
def test_get_pet(db_engine, setup_data, result):
    add_test_data(db_engine, setup_data)

    repo = PostgresPetStoreRepo(db_engine)
    with repo as r:
        pet = r.get_pet(id)
        assert pet == result
