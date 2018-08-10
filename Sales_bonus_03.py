"""
Program to calculate
and display
a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

Rehashed version to support function calls
"""
def main():
    user_input = float(input("Enter sales: $"))
    calculation(user_input)
    print("Bonus: ${:.0f}".format(calculation(user_input)))
    main()

def calculation(sales):
    if sales <1000:
        bonus = sales / 10
    else: bonus = sales / 6.66
    return(bonus)

main()
