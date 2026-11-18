import re


def validate_ticket(ticket: dict) -> bool:
    return bool(ticket.get("ticket_id") and ticket.get("message"))


def extract_order_id(message: str) -> str | None:
    match = re.search(r"#(\d+)", message)

    return match.group(1) if match else None


def classify_ticket(message: str) -> str:
    message_lower = message.lower()

    if "refund" in message_lower:
        return "refund"

    if "order" in message_lower:
        return "order_status"

    if "payment" in message_lower:
        return "payment"

    return "general"


def determine_priority(message: str) -> str:
    message_lower = message.lower()

    if any(word in message_lower for word in ("urgent", "critical", "immediately")):
        return "high"

    return "normal"


def process_ticket(ticket: dict) -> dict:
    if not validate_ticket(ticket):
        raise ValueError("Invalid ticket")

    message = ticket["message"]

    return {
        **ticket,
        "order_id": extract_order_id(message),
        "category": classify_ticket(message),
        "priority": determine_priority(message),
    }
