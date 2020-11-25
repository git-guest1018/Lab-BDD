### calulateRetirement.feature

@calculateRetirement

Feature: Full Retirement Age Calculator
  As a user i want to know what when my retirement date
  is based on my birth date

  Scenario Outline: Calculate the retirement year and month
    Given the user wants to know date to start receiving full SSA benefits
    When "<birth_year>" year is entered
    Then the program will use "<birth_year>" so retirement age will be in "<retire_years>" years and "<retire_months>" months

  Examples:

Examples: Amounts
      | birth_year   | retire_years| retire_months |
      | 1900         | 65        | 0          |
      | 1936         | 65        | 0          |
      | 1937         | 65        | 0          |
      | 1938         | 65        | 2          |
      | 1939         | 65        | 4          |
      | 1940         | 65        | 6          |
      | 1941         | 65        | 8          |
      | 1942         | 65        | 10         |
      | 1943         | 66        | 0          |
      | 1944         | 66        | 0          |
      | 1953         | 66        | 0          |
      | 1954         | 66        | 0          |
      | 1955         | 66        | 2          |
      | 1956         | 66        | 4          |
      | 1957         | 66        | 6          |
      | 1958         | 66        | 8          |
      | 1959         | 66        | 10         |
      | 1960         | 66        | 0          |

 Scenario Outline: Calculate the retirement year and month
    Given the user enters invalid info
    When "<birth_year>" year is invalid
    Then the program will return an invalid message for the "<birth_year>"

    Examples: Amounts
      | birth_year   |
      | 1899         |
      | 2021         |