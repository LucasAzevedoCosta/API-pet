from abc import ABC, abstractmethod

class PersonCreatorControllerInterface(ABC):

    @abstractmethod
    def create(self, person_info: dict) -> dict:
        pass