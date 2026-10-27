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
    """Return the refund due, given the original total and the correct item prices. """
    items_sum = sum(item_prices)
    refund = original - items_sum
    if tax_on: 
        refund *= tax_rate
    return refund