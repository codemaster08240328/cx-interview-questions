Feature: Special Offer (Bogof subset cheapest)

    Rule: "Buy N of {X}, get the cheapest one for free" offer given, where N is a number of products that must be bought, and {X} 
            is a subset of products from the catalogue that this offer is applicable to.

    Rule: The maximum possible discount should be calculated.

    Background:
        Given the following Catalogue:
            | product               | price        |
            | Baked Beans           | 0.99         |
            | Biscuits              | 1.20         |
            | Sardines              | 1.89         |
            | Shampoo (Small)       | 2.00         |
            | Shampoo (Medium)      | 2.50         |
            | Shampoo (Large)       | 3.50         |

        Given the following special Offer:
            | product               | circumstance  | discount  | rule                    |
            | Shampoo               | 3             | 1         | bogof_subset_cheapest   |

        
    Scenario: Scenario 1
        Given the following Basket:
            | product               | quantity     |
            | Shampoo (Large)       | 3            |
            | Shampoo (Medium)      | 1            |
            | Shampoo (Small)       | 2            |

        Then expect a result as following:
            """
            {
                "sub_total": 17.0,
                "discount": 5.50,
                "total": 11.50
            }
            """

    Scenario: Scenario 2

        Given the following Basket:
            | product               | quantity     |
            | Shampoo (Large)       | 2            |
            | Shampoo (Medium)      | 2            |
            | Shampoo (Small)       | 2            |

        Then expect a result as following:
            """
            {
                "sub_total": 16.0,
                "discount": 4.50,
                "total": 11.50
            }
            """
