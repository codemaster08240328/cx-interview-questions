import logging
from .super_market import SuperMarket
from .util import free_discount, percent_discount


class Basket(SuperMarket):
    def __init__(self):
        super(Basket, self).__init__()

        self.total = 0
        self.sub_total = 0
        self.discount = 0
        self.products = {}

    def add_product(self, product, quantity):
        if self.get_product_price(product) == -1:
            logging.error(f"{Product} does not exist in Catalogue.")
        else:
            self.products[product] = quantity
            self.sub_total += self.get_product_price(product) * quantity

    def remove_product(self, product, quantity):
        if quantity >= self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= quantity

        self.sub_total -= self.get_product_price(product * quantity)

    def checkout(self):
        for item in self.products:
            offer = self.get_product_offer(item)
            discount = 0
            if offer:
                if offer["rule"] == "free":
                    discount = free_discount(
                        self.products[item],
                        self.get_product_price(item),
                        offer["discount"],
                        offer["circumstance"],
                    )
                elif offer["rule"] == "percent":
                    discount = percent_discount(
                        self.products[item],
                        self.get_product_price(item),
                        offer["discount"],
                        offer["circumstance"],
                    )

            self.discount += discount

        basket_pricer = {
            "sub_total": self.sub_total,
            "discount": self.discount,
            "total": self.sub_total - self.discount,
        }

        return basket_pricer

    def clear(self):
        super(Basket, self).__init__()
        self.products = {}
        self.total = 0
        self.sub_total = 0
        self.discount = 0
