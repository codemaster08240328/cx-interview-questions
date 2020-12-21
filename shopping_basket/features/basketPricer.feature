Feature: Basket Pricer

    Rule: Basket can contain zero or more products.

    Rule: Basket can not have negative price.

    Rule: Empty Basket should have a sub-total, discount and total each of zero.

    Rule: Maximum possible discount should be calculated.


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
