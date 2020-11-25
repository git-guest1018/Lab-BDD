#### CSC-256-0002
# DisplayRetireMain.py
### Lab-bdd
## Re-writing the earlier to provide my test functionalilty


import sys
from calculateRetirement import *

from calculateRetirement import calculate_retirement_age, calculate_retirement_date


def main():
    print('Social Security Full Retirement Age Calculator')
    inp = 0
    while inp== 0:
        try:
            birth_year = int(input('Enter the year of birth or Enter to exit:'))
            birth_month = int(input('Enter Birth Month as a number:'))
        except ValueError:
            sys.exit()
        retirement_age_year, retirement_age_month = calculate_retirement_age(birth_year)
        retirement_date_year, retirement_date_month = calculate_retirement_date(birth_year, birth_month, retirement_age_year, retirement_age_month)
        month = {1: 'January',
                 2: 'February',
                 3: 'March',
                 4: 'April',
                 5: 'May',
                 6: 'June',
                 7: 'July',
                 8: 'August',
                 9: 'September',
                 10: 'October',
                 11: 'November',
                 12: 'December'}
        print('Your full retirement age is ' + str(retirement_age_year) + ' and ' + str(retirement_age_month) + ' months.')
        print("This will be in {} of {}\n".format(month[retirement_date_month], retirement_date_year))


if __name__ == "__main__":
     main()