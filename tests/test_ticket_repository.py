import pytest

from support_agent.repositories.ticket_repository import (
    TicketRepository,
)


def test_add_and_get_ticket():
    repository = TicketRepository()

    ticket = {
        "ticket_id": 1001,
        "customer_id": 501,
        "category": "order_status",
        "priority": "high",
    }

    repository.add(ticket)

    result = repository.get(1001)

    assert result == ticket


def test_duplicate_ticket_is_rejected():
    repository = TicketRepository()

    ticket = {
        "ticket_id": 1001,
        "customer_id": 501,
        "category": "order_status",
        "priority": "high",
    }

    repository.add(ticket)

    with pytest.raises(ValueError):
        repository.add(ticket)
