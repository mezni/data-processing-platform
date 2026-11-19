from support_agent.services.ticket_processor import (
    classify_ticket,
    extract_order_id,
    process_ticket,
)


def test_extract_order_id():
    assert extract_order_id("My order #4821 has not arrived.") == "4821"


def test_extract_missing_order_id():
    assert extract_order_id("I need a refund.") is None


def test_classify_refund_ticket():
    assert classify_ticket("I need a refund.") == "refund"


def test_process_ticket():
    ticket = {
        "ticket_id": 1001,
        "customer_id": 501,
        "message": "My order #4821 has not arrived.",
    }

    result = process_ticket(ticket)

    assert result["category"] == "order_status"
    assert result["order_id"] == "4821"
    assert result["priority"] == "normal"
