# Simple Tax calculator
# Calculates your weekly, monthly and yearly salary before and after tax.
# Author: Alvin Shi
# Date: 27/5/2018

LAST_UPDATE_TAX = "27/05/2018"
LAST_UPDATE_HELP = "27/05/2018"
LAST_UPDATE_MCL = "02/06/2018"
TAX_THRESHOLDS = (18200, 37000, 87000, 180000)  # Tax Brackets
TAX_RATES = (0.190,  0.325, 0.370, 0.450) # Tax Rate
HELP_THRESHOLDS = (55874, 62239, 68603, 72208, 77619, 84063, 88467, 97378, 103766)
HELP_RATES = (0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08)
MEDICARE_LEVY_RATE = 0.02
TAX_REPORT_COLS = ["TIME INTERVAL", "BEFORE", "AFTER TAX", "TAX"]
HELP_REPORT_COLS = ["TIME INTERVAL", "BEFORE", "AFTER TAX", "AFTER HELP", "TAX", "HELP"]

def get_bool_option(message):
		result = input(message)
		while True:
			if result.lower() in ('y', 'yes'):
				return True
			elif result.lower() in ('n', 'no'):
				return False
			else:
				result = input("Please enter either Y or N. ")

def get_options():
	while True:
		try:
			salary = float(input("Enter yearly salary: $"))
			break
		except ValueError:
			print("Please enter a valid number without special characters except the decimal point")
	has_help = get_bool_option("Do you have a HELP/HECS debt? (Y/N) ")
	medicare_levy = get_bool_option("Do you need to pay Medicare Levy? (Y/N) ")
	return (salary, has_help, medicare_levy)

# If any special characters should be printed, use string except for the case of money
# The float option should only be used in the case of money
def print_table(contents):
	# Padding values arrived at through trial and error
	for content in contents:
		if type(content) == int:
			print("{:15}".format(content), end="")
		elif type(content) == float:
			print("${:<14.2f}".format(content), end="")
		else:
			print("{:15}".format(content), end="")
	print()

def print_brackets(message, brackets, last_update):
	print()
	print(message.upper())
	print("last updated: " + last_update)
	print_table(["BRACKET", "THRESHOLD", "RATE"])
	for number in range (1, len(brackets)+1):
		threshold = brackets[number-1][0]
		rate = brackets[number-1][1]*100
		print_table([str(number), float(threshold), "{:.2f}".format(rate)+"%"])
	print()

def calculate_tax_bracket(remaining_salary, tax_threshold, rate, tax=0):
	taxable_income = remaining_salary - tax_threshold
	if taxable_income > 0:
		tax += taxable_income * rate
		return (tax_threshold, tax)
	else:
		return (remaining_salary, tax)

def calculate_tax(salary, brackets):
	tax = 0
	for (threshold, rate) in reversed(brackets):
		(salary, tax) = calculate_tax_bracket(salary, threshold, rate, tax)
	return tax

def get_rate(brackets, salary):
	for (threshold, rate) in reversed(brackets):
		if threshold < salary:
			return rate
	return 0

def report(message, salary, tax, help_rate=False):
	print()
	print(message.upper())

	salary = float(salary)
	tax = float(tax)
	after_tax = salary - tax
	if help_rate or (type(help_rate) == int and help_rate == 0):
		help_repayment = salary  * help_rate
		after_help = after_tax - help_repayment
		header = HELP_REPORT_COLS
		data = [salary, after_tax, after_help, tax, help_repayment]
	else:
		header = TAX_REPORT_COLS
		data = [salary, after_tax, tax]
	print_table(header)
	print_table(["YEARLY"]  + data)
	print_table(["MONTHLY"] + list(map(lambda x: x/12, data)))
	print_table(["WEEKLY"]  + list(map(lambda x: x/52, data)))


def main():
	tax_brackets = list(zip(TAX_THRESHOLDS, TAX_RATES))
	help_brackets = list(zip(HELP_THRESHOLDS, HELP_RATES))
	print_brackets("CURRENT TAX BRACKET", tax_brackets, LAST_UPDATE_TAX)
	print_brackets("CURRENT HELP BRACKETS", help_brackets, LAST_UPDATE_HELP)

	(base_salary, has_help, medicare_levy) = get_options()
	tax = calculate_tax(base_salary, tax_brackets)
	report_title = "SALARY REPORT WITH TAX"
	help_rate = False
	medicare_rate = False

	if has_help and medicare_levy:
		report_title += ", HELP AND MEDICARE LEVY"
		help_rate = get_rate(help_brackets, base_salary)
		medicare_rate = MEDICARE_LEVY_RATE
	elif has_help:
		report_title += " AND HELP"
		help_rate = get_rate(help_brackets, base_salary)
	elif medicare_levy:
		report_title += " AND MEDICARE LEVY"
		medicare_levy = MEDICARE_LEVY_RATE

	report(report_title, base_salary, tax, help_rate)

if __name__ == '__main__':
	main()
