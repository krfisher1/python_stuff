#assignment 3 cs 1400 task 1#


investment_amount = float(input("Please insert an investment amount "))
print()
monthly_payment_amount = float(input("Please insert a monthly payment amount "))
print()
annual_interest_rate = float(input("please input an annual interest Rate(Entered as a percentage, Example: A rate of 4.5% would be entered as 4.5, not 0.045) "))
print()
number_of_years = float(input("please enter the number of years "))
print()
number_of_months = float(12 * number_of_years)
print()
monthly_interest_rate = float(annual_interest_rate / 12) / 100
print()


left = investment_amount * (1 + monthly_interest_rate ) ** number_of_months

top_of_division = ((1 + monthly_interest_rate) ** (number_of_months) -1)
division_part = top_of_division / monthly_interest_rate
right = monthly_payment_amount * division_part * (1 + monthly_interest_rate)

futurevalue = left + right




print(str(futurevalue))



