import pytest

from calculator import refund_by_totals


def test_refund_by_totals_without_tax():
    assert refund_by_totals(10.00, 8.00, False, 1.0825) == pytest.approx(2.00)

def test_refund_by_totals_with_tax():
    assert refund_by_totals(10.00, 8.00, True, 1.0825) == pytest.approx(2.165)