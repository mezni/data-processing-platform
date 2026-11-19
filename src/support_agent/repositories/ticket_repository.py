from support_agent.domain.ticket import Ticket


class TicketRepository:
    def __init__(self):
        self._tickets: dict[int, Ticket] = {}

    def add(self, ticket: Ticket) -> None:
        if ticket.ticket_id in self._tickets:
            raise ValueError("Duplicate ticket ID")

        self._tickets[ticket.ticket_id] = ticket

    def get(self, ticket_id: int) -> Ticket | None:
        return self._tickets.get(ticket_id)

    def get_all(self) -> list[Ticket]:
        return list(self._tickets.values())

    def count(self) -> int:
        return len(self._tickets)
