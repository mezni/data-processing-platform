from support_agent.ticket_processor import process_ticket


def main() -> None:
    ticket = {
        "ticket_id": 1001,
        "customer": "John",
        "message": "My order #4821 has not arrived.",
        "priority": "high",
    }

    result = process_ticket(ticket)

    print(result)


if __name__ == "__main__":
    main()
