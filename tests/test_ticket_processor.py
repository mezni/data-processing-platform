from support_agent.ticket_processor import (
    classify_ticket,
    extract_order_id,
    process_ticket,
)


def test_classify_order_ticket():
    result = classify_ticket("My order has not arrived")

    assert result == "order_status"


def test_extract_order_id():
    result = extract_order_id("My order #4821 has not arrived")

    assert result == "4821"


def test_extract_missing_order_id():
    result = extract_order_id("My order has not arrived")

    assert result is None


def test_process_ticket():
    ticket = {
        "ticket_id": 1001,
        "customer": "John",
        "message": "My order #4821 has not arrived",
        "priority": "high",
    }

    result = process_ticket(ticket)

    assert result["category"] == "order_status"
    assert result["order_id"] == "4821"
    assert result["needs_order_lookup"] is True
    assert result["status"] == "pending"
