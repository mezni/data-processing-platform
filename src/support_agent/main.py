from support_agent.ticket_repository import TicketRepository


def main():

    repository = TicketRepository()

    tickets = [
        {
            "ticket_id": 1001,
            "customer": "John",
            "category": "order_status",
            "priority": "high",
        },
        {
            "ticket_id": 1002,
            "customer": "Sarah",
            "category": "refund",
            "priority": "normal",
        },
        {
            "ticket_id": 1003,
            "customer": "David",
            "category": "payment_issue",
            "priority": "critical",
        },
        {
            "ticket_id": 1004,
            "customer": "John",
            "category": "refund",
            "priority": "high",
        },
    ]

    for ticket in tickets:
        repository.add(ticket)

    print("Ticket:", repository.get(1001))

    print(
        "High priority:",
        repository.filter_by_priority("high")
    )

    print(
        "Categories:",
        repository.group_by_category()
    )

    print(
        "Customers:",
        repository.get_unique_customers()
    )

    print(
        "Statistics:",
        repository.count_by_priority()
    )


if __name__ == "__main__":
    main()
