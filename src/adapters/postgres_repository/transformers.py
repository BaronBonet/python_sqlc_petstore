from core import domain
from adapters.postgres_repository.generated_queries import models


def pet_to_domain_pet(pet: models.Pet) -> domain.Pet:
    return domain.Pet(
        id=pet.id,
        name=pet.name,
        species=pet.species,
        breed=pet.breed,
        age=pet.age,
        owner_id=pet.owner_id,
        created_at=pet.created_at,
    )
