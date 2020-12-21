import logging
from .super_market import SuperMarket
from .util import bogof_discount, percent_discount


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
            offers = self.get_product_offer(item)
            max_discount = 0
            if offers:
                for offer_item in offers:
                    if offer_item["rule"] == "bogof":
                        discount_t = bogof_discount(
                            self.products[item],
                            self.get_product_price(item),
                            offer_item["discount"],
                            offer_item["circumstance"],
                        )
                        if max_discount < discount_t:
                            max_discount = discount_t
                    elif offer_item["rule"] == "percent":
                        discount_t = percent_discount(
                            self.products[item],
                            self.get_product_price(item),
                            offer_item["discount"],
                            offer_item["circumstance"],
                        )
                        if max_discount < discount_t:
                            max_discount = discount_t

            self.discount += max_discount

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
