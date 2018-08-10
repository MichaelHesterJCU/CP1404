"""
Program to calculate
and display
a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

Rehashed version to support function calls
"""
def calculation(sales):     #takes user input and applies some math to it before returning the data back to the open code.
    if sales <1000:
        bonus = sales / 10
    else: bonus = sales / 6.66
    return(bonus)

user_input = 0      #Avoiding an instant-failure for the while-loop
while user_input > -1:
    user_input = float(input("Enter sales: $"))
    final_bonus = calculation(user_input)       #Calls upon the calculation function and feeds in the user input
    print("Bonus: ${:.0f}".format(final_bonus))
else:
    print("Enter a positive number")
