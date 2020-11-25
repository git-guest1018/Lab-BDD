import pytest
from pytest_bdd import scenarios,parsers,given,when,then

from calculateRetirement import *

EXTRA_TYPES = {
    'Number': int,
}

CONVERTERS = {
    'birth_month': int,
    'birth_year': int,
    'years_to_ssa': int,
    'months_to_ssa': int,
    'retire_month': int,
    'retire_year': int
}
scenarios('../features/calculateRetirement.feature', example_converters=CONVERTERS)

@given(parsers.cfparse('the user wants to know date to start receiving full SSA benefits', extra_types=EXTRA_TYPES))
@given('the user wants to know date to start receiving full SSA benefits')
def test_user_inputs():
    pass


@when(parsers.cfparse('"{birth_year:Number}" year is entered', extra_types=EXTRA_TYPES))
@when('"<birth_year>" year is entered')
def calculate_retirement(birth_year):
    pass


@then(parsers.cfparse('the program will use "{birth_year}" so retirement age will be in "{retire_years}" years and "{retire_months}" months', extra_types=EXTRA_TYPES))
@then('the program will use "<birth_year>" so retirement age will be in "<retire_years>" years and "<retire_months>" months')
def calculate_full_date(birth_year, retire_years, retire_months):
    calc_age = calculate_retirement_age(birth_year)
    assert calc_age[0].__eq__(retire_years)
    assert calc_age[1].__eq__(retire_months)

@given("the user enters invalid info")
def step_impl():
    pass


@when('"<birth_year>" year is invalid')
def input_invalid_year(birth_year):
    pass


@then('the program will return an invalid message for the "<birth_year>"')
def invalid_year_error(birth_year):
    with pytest.raises(ValueError):
        calculate_retirement_age(birth_year)
