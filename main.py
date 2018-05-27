# Simple Tax calculator
# Calculates your weekly, monthly and yearly salary before and after tax.
# Author: Alvin Shi
# Date: 27/5/2018

LAST_UPDATE_TAX = "27/05/2018"
LAST_UPDATE_HELP = "27/05/2018"
TAX_THRESHOLDS = (18200, 37000, 87000, 180000)  # Tax Brackets
TAX_RATES = (0.190,  0.325, 0.370, 0.450) # Tax Rate
HELP_THRESHOLDS = (55874, 62239, 68603, 72208, 77619, 84063, 88467, 97378, 103766)
HELP_RATES = (0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08)

def get_salary():
	while True:
		try:
			salary = float(input("Enter yearly salary: $"))
			break
		except ValueError:
			print("Please enter a valid number without special characters except the decimal point")

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

def tax_help_report(salary, tax, help_rate):
	salary = float(salary)
	tax = float(tax)
	after_tax = salary - tax
	help_repayment = salary  * help_rate
	after_help = after_tax - help_repayment
	print_table(["TIME INTERVAL", "BEFORE", "AFTER TAX", "AFTER HELP", "TAX", "HELP"])
	print_table(["YEARLY", salary, after_tax, after_help, tax, help_repayment])
	print_table(["MONTHLY", salary/12, after_tax/12, after_help/12, tax/12, help_repayment/12])
	print_table(["WEEKLY", salary/52, after_tax/52, after_help/52, tax/52, help_repayment/52])
	print()

def calculate_tax_bracket(remaining_salary, tax_threshold, rate, tax=0):
	taxable_income = remaining_salary - tax_threshold
	if taxable_income > 0:
		tax += taxable_income * rate
		return (tax_threshold, tax)
	else:
		return (remaining_salary, tax)

def calculate_tax_help(message, salary, brackets, help_rate):
	initial_salary = salary
	tax = 0
	print()
	print(message.upper())
	for (threshold, rate) in reversed(brackets):
		(salary, tax) = calculate_tax_bracket(salary, threshold, rate, tax)
	tax_help_report(initial_salary, tax, help_rate)

def get_help_rate(brackets, salary):
	for (threshold, rate) in reversed(brackets):
		if threshold < salary:
			return rate
	return 0

def main():
	tax_brackets = list(zip(TAX_THRESHOLDS, TAX_RATES))
	help_brackets = list(zip(HELP_THRESHOLDS, HELP_RATES))
	print_brackets("CURRENT TAX BRACKET", tax_brackets, LAST_UPDATE_TAX)
	print_brackets("CURRENT HELP BRACKETS", help_brackets, LAST_UPDATE_HELP)

	base_salary = get_salary()
	help_rate = get_help_rate(help_brackets, base_salary)

	calculate_tax_help("NOT INCLUDING SUPER", base_salary, tax_brackets, help_rate)


if __name__ == '__main__':
	main()