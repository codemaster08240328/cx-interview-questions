from behave import fixture
from src.basket import Basket


@fixture
def before_scenario(context, scenario):
    context.basket = Basket()


@fixture
def after_scenario(context, scenario):
    context.basket.clear()
