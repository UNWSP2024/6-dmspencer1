# Title: Tax Rate
# Author: Dalila Spencer
# Date: 2025-10-06

# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program

def calculate_tax(amount, tax_rate):
    tax = amount * tax_rate
    return tax

total_sales = float(input('What is the total sales from this month?: $'))

county_tax = calculate_tax(total_sales, 0.025)
state_tax = calculate_tax(total_sales, 0.05)
print(f'County tax: ${county_tax:,.2f}')
print(f'State tax: ${state_tax:,.2f}')
print(f'Total tax: ${county_tax + state_tax:,.2f}')