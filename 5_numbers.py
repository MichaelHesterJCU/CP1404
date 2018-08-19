"""
A program that asks for 5 numbers and tells the user a few basic facts about the numberss
"""

def main():
    count_down = 5
    list_of_numbers = []
    list_of_facts = []
    loop = 0
    while loop in range(0,5):
        try:
            number = int(input("Please enter {} more number/s:  ".format(count_down)))
            list_of_numbers.append(number)
            loop = loop + 1
            count_down = count_down - 1
        except ValueError:
            print("That wasn't a number".format(count_down))
    list_of_facts.append(sum_of_numbers(list_of_numbers))
    list_of_facts.append(average(list_of_numbers))
    list_of_facts.append(maximum(list_of_numbers))
    list_of_facts.append(minimum(list_of_numbers))
    print("The five numbers are: {}\nThe sum of numbers is: {}\nThe average of the numbers is {}\nThe biggest number is {}\nThe smallest number is {}".format(list_of_numbers,list_of_facts[0],list_of_facts[1],list_of_facts[2],list_of_facts[3]))

def sum_of_numbers(number_list):
    return(sum(number_list))
def average(number_list):
    return(sum_of_numbers(number_list) / 5)
def maximum(number_list):
    return(max(number_list))
def minimum(number_list):
    return(min(number_list))

main()