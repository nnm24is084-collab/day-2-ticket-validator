from datetime import date

from pydantic import ValidationError

from tickets.loader import load_tickets
from tickets.models import Ticket, TicketStatus


def test_valid_ticket():
    ticket = Ticket(
        ticket_id="101",
        customer_name="Anushka",
        service_date="2026-11-24",
        status="open",
    )

    assert ticket.ticket_id == 101
    assert ticket.status == TicketStatus.OPEN


def test_missing_field():
    try:
        Ticket(
            ticket_id=101,
            service_date="2026-11-24",
            status="open",
        )
        assert False, "Expected validation error"
    except ValidationError:
        assert True


def test_bad_date():
    try:
        Ticket(
            ticket_id=101,
            customer_name="Anushka",
            service_date="24-11-2026",
            status="open",
        )
        assert False, "Expected validation error"
    except ValidationError:
        assert True


def test_bad_enum():
    try:
        Ticket(
            ticket_id=101,
            customer_name="Anushka",
            service_date="2026-11-24",
            status="pending",
        )
        assert False, "Expected validation error"
    except ValidationError:
        assert True


def test_empty_file(tmp_path):
    empty_csv = tmp_path / "empty.csv"
    empty_csv.write_text("", encoding="utf-8")

    valid, invalid = load_tickets(empty_csv)

    assert valid == []
    assert invalid == []