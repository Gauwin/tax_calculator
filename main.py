# Command-line tax calculator
# Simple command line tax calculator to break down
# your tax based on your income
#
# Author: Alvin Shi
# Date: 28/03/2019

from tax_brackets_data import *
from user_input import get_settings
from calculate_tax import calculate_tiered_tax, calculate_flat_rate_tax

def zip_brackets(thresholds, rates):
    if len(thresholds) != len(rates):
        return None
    if len(thresholds) == 0:
        return []
    brackets = []
    for i in range(len(thresholds)):
        brackets.append({"threshold": thresholds[i], "rate": rates[i]})
    return brackets


