from support_agent.classifiers.rule_based_classifier import (
    RuleBasedClassifier,
)
from support_agent.domain.ticket import Ticket
from support_agent.repositories.ticket_repository import (
    TicketRepository,
)
from support_agent.services.ticket_service import (
    TicketService,
)


def test_process_ticket():
    service = TicketService(
        classifier=RuleBasedClassifier(),
        repository=TicketRepository(),
    )

    ticket = Ticket(
        ticket_id=1001,
        customer_id=501,
        message="I need a refund.",
    )

    result = service.process(ticket)

    assert result.category == "refund"


def test_ticket_is_saved():
    repository = TicketRepository()

    service = TicketService(
        classifier=RuleBasedClassifier(),
        repository=repository,
    )

    ticket = Ticket(
        ticket_id=1002,
        customer_id=502,
        message="My order is delayed.",
    )

    service.process(ticket)

    assert repository.get(1002) is not None
