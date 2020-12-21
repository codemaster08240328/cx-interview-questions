Feature: Multiple Offer feature

    Rule: One product can have multiple offers

    Rule: Maximum discount should be calculated


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
            | Sardines              | 2             | 20        | percent   |
            | Sardines              | 3             | 30        | percent   |


    Scenario: Scenario 1
        Given the following Basket:
            | product        | quantity     |
            | Sardines       | 2            |

        Then expect a result as following:
            """
            {
                "sub_total": 3.78,
                "discount": 0.76,
                "total": 3.02
            }
            """


    Scenario: Scenario 2
        Given the following Basket:
            | product        | quantity     |
            | Sardines       | 3            |

        Then expect a result as following:
            """
            {
                "sub_total": 5.67,
                "discount": 1.70,
                "total": 3.97
            }
            """

