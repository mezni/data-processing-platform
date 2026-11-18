def calculate_ticket_statistics(
    tickets: list[dict],
) -> dict:
    total = len(tickets)

    priority_counts = {}

    for ticket in tickets:
        priority = ticket["priority"]

        priority_counts[priority] = priority_counts.get(priority, 0) + 1

    return {
        "total_tickets": total,
        "priority_counts": priority_counts,
    }
