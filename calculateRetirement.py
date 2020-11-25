#### CSC-256-0002
# calculateReitement.py
### Lab-bdd
## Re-writing the earlier to provide my test functionalilty
##
from datetime import datetime

CURRENT_YEAR = datetime.today().year
## validating the  user input
## month should be between 1 and 12
## year should be between 1900 and current year
## if the year entered is less than 1900 and greater than current year, program should give error and exit the calculation
def check_age_month(month):
    month = int(month)

    if month < 0 or month >= 12:
        raise ValueError(f'Age month "{month}" must be between 0 and 12')

    return month

def check_age_year(year):
    year = int(year)

    if year < 65 or year > 67:
        raise ValueError(f'Age year "{year}" must be between 65 and 67')

    return year

def check_birth_month(month):
      month = int(month)

      if month < 1 or month > 12:
          raise ValueError(f'Birth month "{month}" must be between 1 and 12')

      return month

###  checking for retirement age based on the birth year
## returned in the value of tuple in  retirement age and month

def calculate_retirement_age(birth_year):
  birth_year = check_birth_year(birth_year)

  if birth_year <= 1937:
    return 65, 0
  elif birth_year == 1938:
    return 65, 2
  elif birth_year == 1939:
    return 65, 4
  elif birth_year == 1940:
    return 65, 6
  elif birth_year == 1941:
    return 65, 8
  elif birth_year == 1942:
    return 65, 10
  elif 1943 <= birth_year <= 1954:
    return 66, 0
  elif birth_year == 1955:
    return 66, 2
  elif birth_year == 1956:
    return 66, 4
  elif birth_year == 1957:
    return 66, 6
  elif birth_year == 1958:
    return 66, 8
  elif birth_year == 1959:
    return 66, 10
  else:
    return 67, 0



def check_birth_year(year):
      year = int(year)
      if year < 1900:
          raise ValueError(f'Birth year "{year}" must be no earlier than 1900')
      elif year >= CURRENT_YEAR:
          raise ValueError(f'Birth year "{year}" must be less than current year')

      return year

def calculate_retirement_date(birth_year, birth_month, age_years, age_months):
    birth_year = check_birth_year(birth_year)
    birth_month = check_birth_month(birth_month)
    age_years = check_age_year(age_years)
    age_months = check_age_month(age_months)

    year = birth_year + age_years
    month = birth_month + age_months

    if month > 12:
        year += 1
        month -= 12

    return year, month