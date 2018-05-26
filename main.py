# Simple Tax calculator
# Calculates your weekly, monthly and yearly salary before and after tax.
# Author: Alvin Shi
# Date: 27/5/2018

# Tax brackets and rates as of 27/05/18
TAX_THRESHOLDS = (18200, 37000, 87000, 18000)  # Tax Brackets
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


def main():
	salary = get_salary()

if __name__ == '__main__':
	main()