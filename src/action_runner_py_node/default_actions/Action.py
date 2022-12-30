from abc import ABC, abstractmethod

class Action(ABC):
    @abstractmethod
    def isFinished(self) -> bool:
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def done(self):
        pass