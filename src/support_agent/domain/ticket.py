from dataclasses import dataclass


@dataclass
class Ticket:
    ticket_id: int
    customer_id: int
    message: str
    category: str = "general"
    priority: str = "normal"
    order_id: str | None = None
