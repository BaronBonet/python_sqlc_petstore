from typing import Optional

import sqlalchemy

from adapters.postgres_repository.generated_queries.petstore import Querier
from adapters.postgres_repository.transformers import pet_to_domain_pet
from core import domain, ports


class PostgresPetStoreRepo(ports.PetStoreRepo):
    def __init__(self, db_engine: sqlalchemy.Engine):
        self.db_engine = db_engine

    def __enter__(self):
        connection = self.db_engine.connect()
        self.connection = connection
        self.querier = Querier(connection)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def get_pet(self, pet_id) -> Optional[domain.Pet]:
        pet = self.querier.get_pet(pet_id=pet_id)
        if not pet:
            return None
        return pet_to_domain_pet(pet)
