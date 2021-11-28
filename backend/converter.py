from decimal import Decimal


def convert(items: str) -> dict:
    """
    Converts portfolio string into usable dictionary value.
    """
    dict = {}
    percentage_sum = 0
    for item in items.split("|"):
        stripped = item.strip()[:-1]
        ticker = stripped.split(' ')[0]
        percentage = stripped.split(' ')[1]
        percentage_sum += Decimal(percentage)
        dict.update({ticker: percentage})
    return dict

