import re


def extract_order_id(message: str) -> str | None:
    match = re.search(r"#(\d+)", message)

    if match:
        return match.group(1)

    return None


def classify_ticket(message: str) -> str:
    message = message.lower()

    if "order" in message or "delivery" in message:
        return "order_status"

    if "refund" in message:
        return "refund"

    if "payment" in message:
        return "payment_issue"

    return "general"


def determine_priority(message: str) -> str:
    message = message.lower()

    if "urgent" in message:
        return "critical"

    if "refund" in message:
        return "high"

    return "normal"


def process_ticket(ticket: dict) -> dict:
    message = ticket["message"]

    category = classify_ticket(message)
    order_id = extract_order_id(message)

    return {
        "ticket_id": ticket["ticket_id"],
        "customer": ticket["customer"],
        "category": category,
        "order_id": order_id,
        "needs_order_lookup": order_id is not None,
        "priority": ticket.get("priority", determine_priority(message)),
        "status": "pending",
    }
