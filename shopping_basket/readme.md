# Documentation

Super Market Shopping Basket pricer component.

## How to run the project (Integration test)

```
$ pipenv install
$ behave
```

## How to use this component

1. Create basket object

```
from src.basket import Basket

basket = Basket()
```

2. Add catalogue

```
basket.add_catalogue(product_name, price)
```

3. Add offer

```
basket.add_offer(product_name, offer)

eg:
(bogof) offer = {
  'circumstance': 2,
  'discount': 1,
  'rule': 'bogof'
}

(percent) offer = {
  'circumstance': 1,
  'discount': 25,
  'rule': 'percent'
}
```

- special offer: basket.add_special_offer(offer)

```
eg. special_offer_bogof_subset:
offer = {
  'product': 'Shampoo',
  'circumstance': 3,
  'discount': 1,
  'rule': 'bogof_subset_cheapest'
}
```

4. Add product to basket

```
basket.add_product(product, quantity)
```

5. Calculate basket price

```
basket.checkout()
```

## Project Structure:

```
| - Shopping Basket
| --- src
      | - basket.py       : `basket` class
      | - super_market.py : `SuperMarket` class
      | - util.py         : utility functions for discount options.

| --- features            : BDD integration test.

```
