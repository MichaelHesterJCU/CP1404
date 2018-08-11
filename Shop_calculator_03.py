"""
    Shop calculator that adds together a number of items determined
    by the user, and then applies a discount if the requirement is
    met.

    Rehashed to support function calls
"""

def main(price):        #Adds the amount of prices together
    cost = sum(price)
    return cost

def discount(regular_cost):     #Applies a discount to the total price when called upon
    discounted_cost = regular_cost - (total_cost / 10)
    return discounted_cost



number_of_items = 0
while number_of_items > -1:
    try:        #Gets the user input for number of items and the cost of the items so long as they're positive numbers
        user_price = []
        number_of_items = int(input("Please enter the number of items: "))
        count = 0
        for count in range(number_of_items):
            count = count + 1
            user_price.append(float(input("Please enter the price of the item: $")))

        total_cost = main(user_price)       #Call upon the main function
        print("Total cost altogether: ${:.2f}".format(total_cost))

        if total_cost >100:
            final_cost = discount(total_cost)       #Call upon the discount function
            print("Final cost: ${:.2f}".format(final_cost))
    except ValueError:
        print("Make sure it's a number")