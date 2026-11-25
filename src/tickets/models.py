from datetime import date
from enum import Enum

from pydantic import BaseModel, ConfigDict, field_validator


class TicketStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"


class Ticket(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ticket_id: int
    customer_name: str
    service_date: date
    status: TicketStatus

    @field_validator("service_date", mode="before")
    @classmethod
    def validate_service_date(cls, value):
        if isinstance(value, date):
            return value

        try:
            return date.fromisoformat(str(value))
        except ValueError as exc:
            raise ValueError("Date must use YYYY-MM-DD format") from exc