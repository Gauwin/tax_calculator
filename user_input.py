def get_y_n_input(message):
    resp = input(message)
    if (resp.lower() in ['y']):
        return True
    elif (resp.lower() in ['n']):
        return False
    else:
        return None

def get_valid_y_n_input(message):
    result = get_y_n_input(message)
    while result is None:
        result = get_y_n_input('Enter either Y or N. ')
    return result

def get_settings():
    def income_from_input(msg, lower_bound = 0):
        user_input = input(msg)
        if not user_input.isnumeric():
            return income_from_input(msg, lower_bound)
        if float(user_input) < lower_bound:
            return lower_bound
        return float(user_input)

    income = \
        income_from_input("Enter your yearly income: $")
    family_income = \
        income_from_input("Enter your yearly family income (0 if N/A): $", income)
    has_help = get_valid_y_n_input("Do you have HECS/HELP? ")

    return (income, family_income, has_help)
