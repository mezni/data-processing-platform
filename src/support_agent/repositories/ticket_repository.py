class TicketRepository:
    def __init__(self):
        self._tickets: dict[int, dict] = {}

    def add(self, ticket: dict) -> None:
        ticket_id = ticket["ticket_id"]

        if ticket_id in self._tickets:
            raise ValueError(f"Ticket {ticket_id} already exists")

        self._tickets[ticket_id] = ticket.copy()

    def get(self, ticket_id: int) -> dict | None:
        ticket = self._tickets.get(ticket_id)

        return ticket.copy() if ticket else None

    def get_all(self) -> list[dict]:
        return [ticket.copy() for ticket in self._tickets.values()]

    def filter_by_priority(
        self,
        priority: str,
    ) -> list[dict]:
        return [
            ticket.copy()
            for ticket in self._tickets.values()
            if ticket["priority"] == priority
        ]

    def group_by_category(self) -> dict[str, list[dict]]:
        grouped = {}

        for ticket in self._tickets.values():
            category = ticket["category"]

            grouped.setdefault(category, []).append(ticket.copy())

        return grouped

    def get_unique_customers(self) -> set[int]:
        return {ticket["customer_id"] for ticket in self._tickets.values()}

    def count_by_priority(self) -> dict[str, int]:
        counts = {}

        for ticket in self._tickets.values():
            priority = ticket["priority"]

            counts[priority] = counts.get(priority, 0) + 1

        return counts
