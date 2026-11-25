import csv
import logging
from pathlib import Path

from pydantic import ValidationError

from tickets.models import Ticket

logger = logging.getLogger(__name__)


def load_tickets(
    file_path: str | Path,
) -> tuple[list[Ticket], list[str]]:

    valid_tickets: list[Ticket] = []
    invalid_rows: list[str] = []

    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            logger.warning("CSV file is empty")
            return valid_tickets, invalid_rows

        for row_number, row in enumerate(reader, start=2):
            try:
                ticket = Ticket.model_validate(row)
                valid_tickets.append(ticket)
                logger.info("Row %s: valid ticket", row_number)

            except ValidationError as error:
                message = f"Row {row_number}: {error}"
                invalid_rows.append(message)
                logger.warning(message)

    return valid_tickets, invalid_rows