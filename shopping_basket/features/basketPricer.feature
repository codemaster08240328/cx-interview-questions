Feature: Basket Pricer

    Rule: Basket can contain zero or more products.

    Rule: Basket can not have negative price.

    Rule: Empty Basket should have a sub-total, discount and total each of zero.

    Rule: Maximum possible discount should be calculated.

    Rule: Three for the 3 of 2 offer should give 6 for the price of 4 offer, 9 for the price of offer.


    Background:
        Given the following Catalogue:
            | product               | price        |
            | Baked Beans           | 0.99         |
            | Biscuits              | 1.20         |
            | Sardines              | 1.89         |
            | Shampoo (Small)       | 2.00         |
            | Shampoo (Medium)      | 2.50         |
            | Shampoo (Large)       | 3.50         |

        Given the following Offer:
            | product               | circumstance  | discount  | rule      |
            | Baked Beans           | 2             | 1         | bogof     |
            | Sardines              | 1             | 25        | percent   |


    Scenario: Scenario 0
        Given empty basket
        Then expect a result as following:
        """
        {
            "sub_total": 0.00,
            "discount": 0.00,
            "total": 0.00
        }
        """

    Scenario: Scenario 1
        Given the following Basket:
            | product        | quantity     |
            | Baked Beans    | 4            |
            | Biscuits       | 1            |

        Then expect a result as following:
            """
            {
                "sub_total": 5.16,
                "discount": 0.99,
                "total": 4.17
            }
            """


    Scenario: Scenario 2
        Given the following Basket:
            | product        | quantity     |
            | Baked Beans    | 2            |
            | Biscuits       | 1            |
            | Sardines       | 2            |

        Then expect a result as following:
            """
            {
                "sub_total": 6.96,
                "discount": 0.95,
                "total": 6.01
            }
            """

    Scenario Outline: Scenario 3, Edge cases for 3 price 2 offer should give 6 price 4 offer and 9 price 6 offer.
        Given the following Basket:
            | product        | quantity     |
            | Baked Beans    | <quantity>   |

        Then expect a result as following
            """
            {
                "sub_total": <sub_total>,
                "discount": <discount>,
                "total": <total>
            }
            """

        Examples:
            | quantity  | sub_total     | discount      | total     |
            | 3         | 2.97          | 0.99          | 1.98      |
            | 6         | 5.94          | 1.98          | 3.96      |
            | 9         | 8.91          | 2.97          | 5.94      |
