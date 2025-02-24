from abc import ABC, abstractmethod

class PetListerControllerInterface(ABC):

    @abstractmethod
    def list(self) -> dict:
        pass