from support_agent.services.ticket_processor import (
    process_ticket,
)
from support_agent.repositories.ticket_repository import (
    TicketRepository,
)
from support_agent.utils.ticket_statistics import (
    calculate_ticket_statistics,
)


def main() -> None:
    repository = TicketRepository()

    raw_tickets = [
        {
            "ticket_id": 1001,
            "customer_id": 501,
            "message": "My order #4821 has not arrived.",
        },
        {
            "ticket_id": 1002,
            "customer_id": 502,
            "message": "I need an urgent refund.",
        },
        {
            "ticket_id": 1003,
            "customer_id": 501,
            "message": "I have a payment issue.",
        },
    ]

    for raw_ticket in raw_tickets:
        processed_ticket = process_ticket(raw_ticket)
        repository.add(processed_ticket)

    tickets = repository.get_all()

    statistics = calculate_ticket_statistics(tickets)

    print("Tickets:")
    for ticket in tickets:
        print(ticket)

    print("\nStatistics:")
    print(statistics)


if __name__ == "__main__":
    main()
