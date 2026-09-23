from decimal import Decimal
import pytest

from src.checkout import calculate_checkout
from src.models import CheckoutRequest, Coupon, LineItem


def D(v: str) -> Decimal:
    return Decimal(v)


def test_checkout_without_shipping():
    req = CheckoutRequest(
        items=(LineItem("A", D("10.00"), 2),),
        tax_rate=D("0.10"),
    )
    result = calculate_checkout(req)
    assert result.subtotal == D("20.00")
    assert result.tax == D("2.00")
    assert result.total == D("22.00")


def test_shipping_is_charged_exactly_once():
    req = CheckoutRequest(
        items=(LineItem("A", D("20.00"), 1),),
        tax_rate=D("0.10"),
        shipping=D("5.00"),
    )
    result = calculate_checkout(req)
    assert result.shipping == D("5.00")
    assert result.total == D("27.00")


def test_percentage_coupon_and_shipping():
    req = CheckoutRequest(
        items=(LineItem("A", D("100.00"), 1),),
        tax_rate=D("0.08"),
        coupon=Coupon("SAVE10", D("10")),
        shipping=D("7.50"),
    )
    result = calculate_checkout(req)
    assert result.discount == D("10.00")
    assert result.tax == D("7.20")
    assert result.total == D("104.70")


def test_non_taxable_items_are_not_taxed_and_discount_is_allocated():
    req = CheckoutRequest(
        items=(
            LineItem("TAXABLE", D("80.00"), 1, taxable=True),
            LineItem("EXEMPT", D("20.00"), 1, taxable=False),
        ),
        tax_rate=D("0.10"),
        coupon=Coupon("SAVE10", D("10")),
    )
    result = calculate_checkout(req)
    assert result.discount == D("10.00")
    assert result.tax == D("7.20")
    assert result.total == D("97.20")


def test_empty_cart_rejected():
    with pytest.raises(ValueError):
        calculate_checkout(CheckoutRequest(items=(), tax_rate=D("0.10")))


def test_invalid_quantity_rejected():
    with pytest.raises(ValueError):
        calculate_checkout(CheckoutRequest(
            items=(LineItem("A", D("1.00"), 0),), tax_rate=D("0.10")
        ))
