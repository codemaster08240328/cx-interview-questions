from decimal import Decimal


class SuperMarket:
    """
    catalogue: {
        'Backed Beans': 0.99,
        'Biscuits': 1.20,
        'Sardines': 1.89,
        'Shampoo (small)': 2.00,
        'Shampoo (medium)': 2.50,
        'Shampoo (large)': 3.50
    }

    offer: {
        'Backed Beans': [{
            'circumstance': 2,
            'discount': 1,
            'rule': 'bogof'
        }],
        'Sardines': [{
            'circumstance': 1,
            'discount': 25,
            'rule': 'percent'
        }, {
            'circumstance': 2,
            'discount': 30,
            'rule': 'percent'
        }]
    }
    """

    def __init__(self):
        self.catalogue = {}
        self.offer = {}

    def add_catalogue(self, product, price):
        self.catalogue[product] = round(Decimal(float(price) + 0.001), 2)

    def add_offer(self, product, offer):
        if product in self.offer:
            self.offer[product].append(offer)
        else:
            self.offer.update({product: [offer]})

    def add_special_offer(self, offer):
        if "special" in self.offer:
            self.offer["special"].append(offer)
        else:
            self.offer.update({"special": [offer]})

    def get_product_price(self, product):
        try:
            return self.catalogue[product]

        except Exception as e:
            return -1

    def get_product_offer(self, product):

        try:
            return self.offer[product]
        except Exception as e:
            return 0
