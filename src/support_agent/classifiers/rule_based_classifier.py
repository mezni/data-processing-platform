from support_agent.interfaces.ticket_classifier import (
    TicketClassifier,
)


class RuleBasedClassifier(TicketClassifier):
    def classify(self, message: str) -> str:
        message = message.lower()

        if "refund" in message:
            return "refund"

        if "order" in message:
            return "order_status"

        if "payment" in message:
            return "payment"

        return "general"
