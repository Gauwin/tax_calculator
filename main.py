# Simple Tax calculator
# Calculates your weekly, monthly and yearly salary before and after tax.
# Author: Alvin Shi
# Date: 27/5/2018

LAST_UPDATE = "27/05/2018"
TAX_THRESHOLDS = (18200, 37000, 87000, 180000)  # Tax Brackets
RATES = (0.190,  0.325, 0.370, 0.450) # Tax Rate


def calculate_tax(remaining_salary, tax_threshold, rate, tax=0):
	taxable_income = remaining_salary - tax_threshold
	if taxable_income > 0:
		tax += taxable_income * rate
		return (tax_threshold, tax)
	else:
		return (remaining_salary, tax)

def get_salary():
	while True:
		try:
			return float(input("Enter yearly salary: $"))
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

def print_brackets(brackets):
	print()
	print("CURRENT TAX BRACKET")
	print("last updated: " + LAST_UPDATE)
	print_table(["BRACKET", "THRESHOLD", "RATE"])
	for number in range (1, len(brackets)+1):
		threshold = brackets[number-1][0]
		rate = brackets[number-1][1]*100
		print_table([str(number), float(threshold), str(rate)+"%"])
	print()

def tax_report(salary, tax):
	print()
	print_table(["TIME INTERVAL", "BEFORE", "AFTER"])
	print_table(["YEARLY", "$" + str(float(salary)), "$" + str(float(salary-tax))])

def main():
	salary = get_salary()
	initial_salary = salary
	tax = 0
	brackets = list(zip(TAX_THRESHOLDS, RATES))

	print_brackets(brackets)
	for (threshold, rate) in reversed(brackets):
		(salary, tax) = calculate_tax(salary, threshold, rate, tax)
	tax_report(initial_salary, tax)

if __name__ == '__main__':
	main()