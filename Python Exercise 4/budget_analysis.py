import pandas as pd

# get budget dataset
budget = pd.read_csv('national-budget.csv')

def get_budget(year: int, office: str = None) -> int:
    """
    Gets the budget, of a given office or the entire budget, in a specific year

    examples:
    >>> get_budget(1997)
    186045315000
    >>> get_budget(1997, 'בריאות')
    11017315000
    >>> get_budget(2000, 'אין_משרד_כזה')
    Traceback (most recent call last):
        ...
    ValueError: There is no data on the office אין_משרד_כזה
    """
    if year not in budget['שנה'].unique():
        raise ValueError(f'There is no data on the year {year}')
    if office and office not in budget['שם רמה 2'].unique():
        raise ValueError(f'There is no data on the office {office}')

    if office:
        budget_ = budget.loc[(budget['שם רמה 2'] == office)
                             & (budget['שנה'] == year)
                             & (budget['הוצאה/הכנסה'] == 'הוצאה')
                             & (budget['סוג תקציב'] == 'מאושר')]
    else:
        budget_ = budget.loc[(budget['שנה'] == year)
                             & (budget['הוצאה/הכנסה'] == 'הוצאה')
                             & (budget['סוג תקציב'] == 'מאושר')]

    return int(budget_['הוצאה נטו'].sum()) * 1000


def education_budget(year: int) -> int:
    """
    Gets the total education budget in a given year

    examples:
    >>> education_budget(1997)
    19320620000
    >>> education_budget(2100)
    Traceback (most recent call last):
        ...
    ValueError: There is no data on the year 2100
    """
    return get_budget(year, 'חינוך')


def security_budget_ratio(year: int) -> float:
    """
    Gets the security budget in a given year, as a percentage of that year's total budget.

    examples:
    >>> security_budget_ratio(1997)
    0.20096286756804385
    >>> security_budget_ratio(2100)
    Traceback (most recent call last):
        ...
    ValueError: There is no data on the year 2100
    """
    # get the security budget for a specific year and the overall budget
    security_budget = get_budget(year, 'בטחון')
    overall_budget = get_budget(year)

    # return ratio
    return security_budget / overall_budget


def largest_budget_year(office: str) -> int:
    """
    Gets the year in which the budget of a given office was the largest.

    examples:
    >>> largest_budget_year('בריאות')
    2021
    >>> largest_budget_year('אין_משרד_כזה')
    Traceback (most recent call last):
        ...
    ValueError: There is no data on the office אין_משרד_כזה
    """
    # create a dictionary of all years and their budget
    budget_dict = {}
    for year in budget['שנה'].unique():
        budget_dict[year] = get_budget(year, office)

    # find the max budget and return its year
    return max(budget_dict, key=budget_dict.get)


def budget_difference(year: int, office: str = None) -> float:
    """
    Gets the difference in the budget (of a given office or the entire budget) of a given year
    in relation to the year preceding it

    example 1: the entire budget in 2016 increased by 9%
    >>> budget_difference(2016)
    0.09363775641203399

    example 2: the health budget in 2020 inecreased by 26%
    >>> budget_difference(2020, 'בריאות')
    0.26526068941785685
    """
    # gets the budget, of a specific office or the entire budget, for a specific year and the year preceding it
    cur_budget = get_budget(year, office)
    prev_budget = get_budget(year - 1, office)

    # return the difference in the budget
    return (cur_budget - prev_budget) / prev_budget


if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    print(budget.shape)
    print(budget.head(10))

    import doctest
    print(doctest.testmod())
