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


def main() -> None:
    classifier = RuleBasedClassifier()
    repository = TicketRepository()

    service = TicketService(
        classifier=classifier,
        repository=repository,
    )

    ticket = Ticket(
        ticket_id=1001,
        customer_id=501,
        message="My order #4821 has not arrived.",
    )

    processed_ticket = service.process(ticket)

    print(processed_ticket)
    print(f"Stored tickets: {repository.count()}")


if __name__ == "__main__":
    main()
