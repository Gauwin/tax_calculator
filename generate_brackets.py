from tax_brackets_data import *

def generate_brackets(thresholds, rates):
    if len(thresholds) != len(rates):
        return None
    if len(thresholds) == 0:
        return []
    brackets = []
    for i in range(len(thresholds)):
        brackets.append({"threshold": thresholds[i], "rate": rates[i]})
    return brackets

def get_income_tax_brackets():
    return generate_brackets(TAX_THRESHOLDS, TAX_RATES)

def get_hecs_brackets():
    return generate_brackets(HELP_THRESHOLDS, HELP_RATES)

def get_medicare_levy_brackets():
    return generate_brackets(MEDICARE_LEVY_THRESHOLD, MEDICARE_LEVY_RATE)
