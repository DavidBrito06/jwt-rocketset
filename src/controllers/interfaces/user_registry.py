from abc import ABC, abstractmethod

class UserRegistryInterface(ABC):
    @abstractmethod
    def registry(self, username: str, password: str) -> dict:
        pass