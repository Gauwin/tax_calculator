# Simple Tax calculator
# Calculates your weekly, monthly and yearly salary before and after tax.
# Author: Alvin Shi
# Date: 27/5/2018

LAST_UPDATE = "27/05/2018"
TAX_THRESHOLDS = (18200, 37000, 87000, 180000)  # Tax Brackets
TAX_RATES = (0.190,  0.325, 0.370, 0.450) # Tax Rate
SUPER_PERCENT = 1.095

def get_salary():
	while True:
		try:
			salary = float(input("Enter yearly salary: $"))
			break
		except ValueError:
			print("Please enter a valid number without special characters except the decimal point")
	super_included = input("Is this your salary including super? (Y/N) ")
	while True:
		if super_included.lower() in ('y', 'yes'):
			super_included = True
			break
		elif super_included.lower() in ('n', 'no'):
			super_included = False
			break
		else:
			super_included = input("Please enter either Y or N. ")
	if super_included:
		return salary / SUPER_PERCENT
	return salary 

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

def print_brackets(brackets):
	print()
	print("CURRENT TAX BRACKET")
	print("last updated: " + LAST_UPDATE)
	print_table(["BRACKET", "THRESHOLD", "RATE"])
	for number in range (1, len(brackets)+1):
		threshold = brackets[number-1][0]
		rate = brackets[number-1][1]*100
		print_table([str(number), float(threshold), "{:.2f}".format(rate)+"%"])
	print()

def tax_report(salary, tax):
	salary = float(salary)
	tax = float(tax)
	after_tax = salary - tax
	print_table(["TIME INTERVAL", "BEFORE", "AFTER TAX", "TAX"])
	print_table(["YEARLY", salary, after_tax, tax])
	print_table(["MONTHLY", salary/12, after_tax/12, tax/12])
	print_table(["WEEKLY", salary/52, after_tax/52, tax/52])
	print()

def calculate_tax_bracket(remaining_salary, tax_threshold, rate, tax=0):
	taxable_income = remaining_salary - tax_threshold
	if taxable_income > 0:
		tax += taxable_income * rate
		return (tax_threshold, tax)
	else:
		return (remaining_salary, tax)

def calculate_tax(message, salary, brackets):
	initial_salary = salary
	tax = 0

	print()
	print(message.upper())
	for (threshold, rate) in reversed(brackets):
		(salary, tax) = calculate_tax_bracket(salary, threshold, rate, tax)
	tax_report(initial_salary, tax)


def main():
	brackets = list(zip(TAX_THRESHOLDS, TAX_RATES))
	print_brackets(brackets)

	base_salary = get_salary()

	calculate_tax("NOT INCLUDING SUPER", base_salary, brackets)


if __name__ == '__main__':
	main()