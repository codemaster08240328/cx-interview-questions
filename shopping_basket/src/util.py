from decimal import Decimal


def percent_discount(item_q, item_p, percentage, circum):
    if item_q >= circum:
        return round(Decimal(float(item_q * item_p * percentage / 100) + 0.001), 2)
    else:
        return 0


def bogof_discount(item_q, item_p, free_c, circum):
    if item_q >= circum + free_c:
        free_c = int(item_q / (circum + free_c)) * free_c
        return round(Decimal(float(free_c * item_p) + 0.001), 2)
    else:
        return 0
