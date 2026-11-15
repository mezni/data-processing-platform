from collections import defaultdict


class TicketRepository:

    def __init__(self):
        self._tickets: dict[int, dict] = {}

    def add(self, ticket: dict) -> None:
        ticket_id = ticket["ticket_id"]

        if ticket_id in self._tickets:
            raise ValueError(
                f"Ticket {ticket_id} already exists"
            )

        self._tickets[ticket_id] = ticket

    def get(self, ticket_id: int) -> dict | None:
        return self._tickets.get(ticket_id)

    def get_all(self) -> list[dict]:
        return list(self._tickets.values())

    def filter_by_priority(
        self,
        priority: str
    ) -> list[dict]:

        return [
            ticket
            for ticket in self._tickets.values()
            if ticket["priority"] == priority
        ]

    def group_by_category(self) -> dict[str, list[dict]]:
        grouped = defaultdict(list)

        for ticket in self._tickets.values():
            category = ticket.get("category", "general")
            grouped[category].append(ticket)

        return dict(grouped)

    def get_unique_customers(self) -> set[str]:
        return {
            ticket["customer"]
            for ticket in self._tickets.values()
            if ticket.get("customer")
        }

    def count_by_priority(self) -> dict[str, int]:
        counts: dict[str, int] = defaultdict(int)

        for ticket in self._tickets.values():
            counts[ticket["priority"]] += 1

        return dict(counts)
