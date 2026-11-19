from abc import ABC, abstractmethod


class TicketClassifier(ABC):
    @abstractmethod
    def classify(self, message: str) -> str:
        pass
