def refund_by_totals(
    original: float, desired: float, tax_on: bool, tax_rate: float
) -> float:
    """Return the refund due, given the original and correct totals."""
    refund = original - desired
    if tax_on:
        refund *= tax_rate
    return refund


def refund_by_items(
    item_prices: list[float], original: float, tax_on: bool, tax_rate: float
) -> float:
    """Return the refund due, given the original total and the correct item prices."""
    items_sum = sum(item_prices)
    refund = original - items_sum
    if tax_on:
        refund *= tax_rate
    return refund


def combo_upgrade_cost(
    combo_price: float, sandwich: float, side: float
) -> float:
    """Return the amount to charge to upgrade a sandwich and side to a full combo."""
    price_of_items = sandwich + side
    return combo_price - price_of_items