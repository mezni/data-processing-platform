from support_agent.domain.ticket import Ticket
from support_agent.interfaces.ticket_classifier import (
    TicketClassifier,
)
from support_agent.repositories.ticket_repository import (
    TicketRepository,
)


class TicketService:
    def __init__(
        self,
        classifier: TicketClassifier,
        repository: TicketRepository,
    ):
        self.classifier = classifier
        self.repository = repository

    def process(self, ticket: Ticket) -> Ticket:
        category = self.classifier.classify(ticket.message)

        ticket.category = category

        self.repository.add(ticket)

        return ticket
