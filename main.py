# Command-line tax calculator
# Simple command line tax calculator to break down
# your tax based on your income
#
# Author: Alvin Shi
# Date: 28/03/2019

import tax_brackets_data

def zip_brackets(thresholds, rates):
    if len(thresholds) is not len(rates):
        return None
    if len(thresholds) is 0:
        return []
    brackets = []
    for i in range(len(thresholds)):
        brackets.append({"threshold": thresholds[i], "rate": rates[i]})
    return brackets

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

def flat_rate_tax_calculator(income, sorted_brackets):
    taxed = 0
    for pair in sorted_brackets[::-1]:
        threshold = pair["threshold"]
        if threshold < income:
            taxed = income * pair["rate"]
            break
    return (income - taxed, taxed)
