import json
from decimal import Decimal
from behave import *
from src.basket import Basket


@given("the following Catalogue")
def step_impl(context):
    for row in context.table:
        context.basket.add_catalogue(row["product"], row["price"])


@given("the following Offer")
def step_impl(context):
    for row in context.table:
        context.basket.add_offer(
            row["product"],
            {
                "circumstance": int(row["circumstance"]),
                "discount": int(row["discount"]),
                "rule": row["rule"],
            },
        )


@given("the following Basket")
def step_impl(context):
    for row in context.table:
        context.basket.add_product(row["product"], int(row["quantity"]))


@then("expect a result as following")
def step_impl(context):
    expected_result = json.loads(context.text)
    actual_result = context.basket.checkout()

    assert (
        round(Decimal(float(expected_result["total"]) + 0.001), 2)
        == actual_result["total"]
    )
    assert (
        round(Decimal(float(expected_result["discount"]) + 0.001), 2)
        == actual_result["discount"]
    )
    assert (
        round(Decimal(float(expected_result["sub_total"]) + 0.001), 2)
        == actual_result["sub_total"]
    )
