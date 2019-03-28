# Command-line tax calculator
# Simple command line tax calculator to break down
# your tax based on your income
#
# Author: Alvin Shi
# Date: 28/03/2019

def calculate_tax(income, sorted_brackets):
    taxed = 0
    last_threshold = income
    for pair in sorted_brackets[::-1]:
        threshold = pair["threshold"]
        tax_amount = last_threshold - threshold

        if tax_amount <= 0:
            continue

        last_threshold = threshold
        taxed += tax_amount * pair["rate"]
    return (income - taxed, taxed)
