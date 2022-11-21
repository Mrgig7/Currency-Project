from decimal import Decimal
from functools import reduce


def average(*items):
    """
    Returns mean average of a list (expects Decimal objects).
    """
    return reduce(lambda x, y: x+y, items) / Decimal(len(items))


{
    'USD': {
        'GBP': Decimal('0.6666667'),
        'EUR': Decimal('0.94'),
        'CNY': Decimal('6.39'),
    }
}


def invert(fro, to):
    """
    Given two arguments, one which is the amount of the base currency (normally
    1.00) and the second which is the amount of the other currency you get for
    that amount, return the reverse conversion rate i.e. amount of fro I can
    get for 1.00 of to.
    """
    return fro/to, to/to


def convert_others(currency_dict):
    """
    Where currency_dict is a dict with one key representing the exchange rates
    of one currency, return another dict with all the exchange rates between
    all currencies in the dict.
    NOTE: Undefined behaviour if more than one top-level key in the dict.
    """
    # new dictionary to eventually store results
    results_dict = {}
    # pop one item out of dict
    master, rates = currency_dict.popitem()
    # put this list of already calculated rates into the results dict
    results_dict[master] = rates
    # store list of currencies
    currencies = set([master] + [k for k in rates.keys()])
    # for each given rate, calculate inverse rate to master currency
    for currency, rate in rates.items():
        results_dict[currency] = {}
        results_dict[currency][master] = invert(Decimal('1.00'), rate)[0]
    # now fill in all other rates
    for base in currencies:
        for other in currencies:
            if (base != other) and (master != other) and (base != master):
                # actually calculate the rate
                from_rate = results_dict[base][master]
                to_rate = results_dict[master][other]
                results_dict[base][other] = from_rate * to_rate

    return results_dict


convert_others(
    {
        'USD': {
            'GBP': Decimal('0.6666667'),
            'EUR': Decimal('0.94'),
            'CNY': Decimal('6.39'),
        }
    }
)