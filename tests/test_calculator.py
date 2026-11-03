import pytest

from calculator import (
    refund_by_totals,
    refund_by_items,
    combo_upgrade_cost,
    parse_prices,
)


def test_refund_by_totals_without_tax():
    assert refund_by_totals(10.00, 8.00, False, 1.0825) == pytest.approx(2.00)


def test_refund_by_totals_with_tax():
    assert refund_by_totals(10.00, 8.00, True, 1.0825) == pytest.approx(2.165)


def test_refund_by_items_without_tax():
    assert refund_by_items([2.00, 2.50, 1.00], 10.00, False, 1.0825) == pytest.approx(
        4.50
    )


def test_refund_by_items_with_tax():
    assert refund_by_items([2.00, 2.50, 1.00], 10.00, True, 1.0825) == pytest.approx(
        4.87125
    )


def test_combo_upgrade_cost():
    assert combo_upgrade_cost(8.50, 5.00, 2.5) == pytest.approx(1.00)


def test_parse_prices_empty():
    assert parse_prices("") == []


def test_parse_prices_normal():
    assert parse_prices("2.00, 2.50, 1.00") == [2.0, 2.5, 1.0]


def test_parse_prices_bad_input():
    with pytest.raises(ValueError):
        parse_prices("abc")
