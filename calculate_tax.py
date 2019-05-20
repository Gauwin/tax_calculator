def calculate_tiered_tax(income, sorted_brackets):
    taxed = 0
    last_threshold = income
    for pair in sorted_brackets[::-1]:
        threshold = pair["threshold"]
        tax_amount = last_threshold - threshold

        if tax_amount <= 0:
            continue

        last_threshold = threshold
        taxed += tax_amount * pair["rate"]
    return taxed

def calculate_flat_rate_tax(income, sorted_brackets):
    taxed = 0
    for pair in sorted_brackets[::-1]:
        threshold = pair["threshold"]
        if threshold < income:
            taxed = income * pair["rate"]
            break
    return taxed
