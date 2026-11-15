import pytest

from support_agent.ticket_repository import TicketRepository


@pytest.fixture
def repository():
    repo = TicketRepository()

    repo.add(
        {
            "ticket_id": 1001,
            "customer": "John",
            "category": "refund",
            "priority": "high",
        }
    )

    repo.add(
        {
            "ticket_id": 1002,
            "customer": "Sarah",
            "category": "order_status",
            "priority": "normal",
        }
    )

    return repo


def test_get_ticket(repository):
    ticket = repository.get(1001)

    assert ticket["customer"] == "John"


def test_missing_ticket(repository):
    assert repository.get(9999) is None


def test_filter_by_priority(repository):
    result = repository.filter_by_priority("high")

    assert len(result) == 1
    assert result[0]["ticket_id"] == 1001


def test_group_by_category(repository):
    result = repository.group_by_category()

    assert "refund" in result
    assert "order_status" in result


def test_unique_customers(repository):
    result = repository.get_unique_customers()

    assert result == {"John", "Sarah"}


def test_duplicate_ticket(repository):
    with pytest.raises(ValueError):
        repository.add(
            {
                "ticket_id": 1001,
                "customer": "John",
                "category": "refund",
                "priority": "high",
            }
        )
