from abc import ABC, abstractmethod
from typing import Optional

from core import domain


class PetStoreRepo(ABC):
    @abstractmethod
    def get_pet(self, pet_id: int) -> Optional[domain.Pet]:
        pass

    # @abstractmethod
    # def get_pets(self) -> list[domain.Pet]:
    #     pass
    #
    # @abstractmethod
    # def add_pet(self, pet: domain.Pet) -> None:
    #     pass
    #
    # @abstractmethod
    # def delete_pet(self, pet_id: int) -> None:
    #     pass
