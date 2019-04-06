# Command-line tax calculator
# Simple command line tax calculator to break down
# your tax based on your income
#
# Author: Alvin Shi
# Date: 28/03/2019

from tax_brackets_data import *
from user_input import get_settings
from calculate_tax import \
    calculate_tiered_tax, calculate_flat_rate_tax
from generate_brackets import \
    get_income_tax_brackets, get_hecs_brackets, get_medicare_levy_brackets

def main():
    tax_brackets = get_income_tax_brackets()
    hecs_brackets = get_hecs_brackets()
    medicare_brackets = get_medicare_levy_brackets()
    # medicare_surcharge = generate_brackets(MEDICARE_SURCHARGE_THRESHOLD, MEDICARE_SURCHARGE_RATE)
    (income, family_income, has_help) = get_settings()
    # OUTPUT
    # [income, tax, hecs, medicare, after_tax]
    (after_tax, tax) = calculate_tiered_tax(income, tax_brackets)
    (after_hecs, hecs) = calculate_flat_rate_tax(income, hecs_brackets)
    (after_medicare, medicare) = calculate_flat_rate_tax(income, medicare_brackets)
    post_tax = income - tax - hecs - medicare
    print([income, tax, hecs, medicare, post_tax])


if __name__ == '__main__':
    main()
