"""
STARTER CODE
Homework 2: Ice Cream Stand
Topics Covered:
- Lists (append, pop)
- For and while loops
- Getting user inputs
- Validating user inputs
- Functions and helper functions
- Formatted Strings
"""
import random
# TODO: Students, fill out statement of work header
# Student Name in Canvas: Tony Marsalla
# Penn ID: 50053305
# Did you do this homework on your own (yes / no): yes
# Resources used outside course materials:

# import statements
from random import randint, choice


def print_welcome_and_menu(list_of_flavors, list_of_sizes, list_of_prices):
    """
    Prints the following:
    1. Welcome message (Must contain word 'welcome')
    2. Message on what flavors are available in the ice cream store.
        Hint: Loop through the list_of_flavors
    3. Message on how much each size cost.
        Hint: Loop through the list_of_sizes, list_of_prices
        Format should be: Our {size} ice cream is ${price}.
    """
    # TODO: Write your code here
    print("Welcome to Penn's Student Run Ice Cream Stand!\n") #make sure to put the parameters in when you call this.
    print("Our current flavors for today are:")
    #create a list of flavors
    # you have to call this in the main function - list_of_flavors = ['Vanilla', 'Chocolate', 'Strawberry']
    for flavors in list_of_flavors:
        print (flavors)
    #I look up \r to fix the issue with spacing after strawberry. \n was generating 2 lines and not having anything at all was to no spaces between the line.
    print("\r")
    #for sizes and price, you have to put them in the same loop. Small = 4.99, medium = $7.49, large = $8.49
    #also, you have to re-create the list for both so they don't print altogther.

    #since sizes and prices are of differet data types, range(len), must be used to convert both of them to indicies.
    #Since both are converted to indices, a new variable is needed, hence "combine".
    for combine in range(len(list_of_sizes)): #indexed 0, 1, and 2
        size = list_of_sizes[combine] #here, I grab the elements at the same index (0,1,2) and print each indicies together during each iteration.
        price = list_of_prices[combine]
        print("Our {} ice cream is ${}".format(size, price))

  # TODO: Remove the pass statement once you have your code written


def get_order_qty(customer_name):
    """
    Ask the customer how many orders of ice cream they want.
    Valid order quantity should be an integer 1-5 inclusive. If outside the range or non-int, re-prompt.
    Hint: When asking for user input, cast it to an integer. If the input cannot be cast-ed to an integer, re-prompt.
    If the input is a float, Example: 2.54 will return 2 and follow the rules of string to integer casting.
    Returns: How many orders of ice cream the customer wants.
    """
    order_qty = 0
    # TODO: Write your code here
    while True: #loop is necessary becuase if user enter invalid input, it will not re-prompt.
        order_qty = input("How many ice creams will you be ordering (1 to 5)? ")
        try:
            order_qty = int(order_qty)
            if 1 <= order_qty <= 5:
                break #if the customer enters a number 1 to 5, I want to exit this loop as it's no longer needed.
        except ValueError as e:
            print("Please enter a valid integer.")
            print (e)
    return order_qty


def get_ice_cream_flavor(ice_cream_flavors):
    """
    Ask the customer 'Which flavor would you like (v/c/s)? '
    Then, processes and cleans the input and returns the equivalent flavor from ice_cream_flavors list.
    Hint:   Use the indices set in the main function for the flavors.
            Call the get_first_letter_of_user_input function to get and process inputs.
            Note: Only the first letter of the input will be considered so an input of 'Cookies and Cream'
            will be considered as 'c' which corresponds to 'Chocolate'.
            Ask again if it is not a valid flavor.
    Returns: String of ice cream flavor picked (e.g "Vanilla")
    """

    flavor_picked = ""
    # TODO: Write your code here
    #only break out of the loop if the user selects the correct input. Otherwise, re-prompt.
    while True:
        flavor_picked = get_first_letter_of_user_input("Which flavor would you like (v/c/s)? ")
        '''The code below I originally tried and didn't run correctly:
                 if flavor_picked == 'v':
                    flavor_picked = ice_cream_flavors[0]
                    break
            for future studying, the reason you can't do this, is because when 
             you set flavor_picked  = ice_cream_flavors[0], your overwriting the user input and the
             loop won't exit because it thinks you still need to enter an input.'''
        if flavor_picked == 'v':
            return ice_cream_flavors[0]
        elif flavor_picked == 'c':
            return ice_cream_flavors[1]
        elif flavor_picked == 's':
            return ice_cream_flavors[2]
            #return flavor_picked isn't necessary since it will automatically do that
        else:
            continue
            # return flavor_picked isn't necessary since it will automatically do that


def get_ice_cream_size(ice_cream_sizes):
    """
    Ask the customer 'Which size would you like (s/m/l)? '
    Then, processes and cleans the input and returns the equivalent size from ice_cream_sizes list.
    Hint:   Use the indices set in the main function for the sizes.
            Call the get_first_letter_of_user_input function to get and process inputs.
            Note: Only the first letter of the input will be considered so an input of 'Super Large'
            will be considered as 's' which corresponds to 'Small'.
            Ask again if it is not a valid size.
    Returns: String of Size picked (e.g "Small")
    """
    size_picked = ""
    # TODO: Write your code here
    # only break out of the loop if the user selects the correct input. Otherwise, re-prompt.
    while True:
        size_picked = get_first_letter_of_user_input("Which size would you like (s/m/l)? ")
        if size_picked == "s":
            return ice_cream_sizes[0]
        elif size_picked == 'm':
            return ice_cream_sizes[1]
        elif size_picked == "l":
            return ice_cream_sizes[2]
    # return flavor_picked isn't necessary since it will automatically do that
        else:
            continue
    # return size_picked isn't necessary since it will automatically do that


def get_ice_cream_order_price(ice_cream_size, ice_cream_prices, ice_cream_sizes):
    """
    Hint:   Use the indices set in the main function for the prices of Small, Medium and Large.
    Returns: The equivalent price of an ice cream size. Example: Returns 4.99 if ice_cream_size is 'Small'
    """
    # TODO: Write your code here
    if ice_cream_size == ice_cream_sizes[0]:
        return ice_cream_prices[0]
    elif ice_cream_size == ice_cream_sizes[1]:
        return ice_cream_prices[1]
    elif ice_cream_size == ice_cream_sizes[2]:
        return ice_cream_prices[2]

def take_customer_order(customer_name, ice_cream_flavors, ice_cream_sizes, ice_cream_prices):
    """
    This function runs when a customer reaches the front of the queue. It should print
    the current customer's name being served, and take their order(s).
    If the customer can pay for their order, returns the amount of revenue from the sale.
    If the customer cancels their order, returns 0.
    Hint: Use other helper functions we required you to write whenever needed here.
    Returns: Amount of Revenue from the sale with customer
    """

    total_bill = 0

    # TODO: Print a message "Now serving customer: X" where X is the current customer's name
    print("Now Serving Customer:", customer_name)
    # TODO: Call the get_order_qty and save the value to order_qty
    order_qty = get_order_qty(customer_name)

    # TODO: For Each order you need to get a flavor, and size
    for order in range(order_qty): #this start at 1 and iterate to the up-to value including it.
        print("Order No:", order + 1)
        # TODO: Write code to get the ice cream flavor for this order
        flavor = get_ice_cream_flavor(ice_cream_flavors)
        # TODO: Write code to get the ice cream size for this order
        size = get_ice_cream_size(ice_cream_sizes)
        # TODO: Write code to get the price for this order
        price = get_ice_cream_order_price(size,ice_cream_prices,ice_cream_sizes)
        # TODO: Update the total_bill
        total_bill += price
        # TODO: Print the details for this order
        #   Hint: See https://www.w3schools.com/python/python_string_formatting.asp for string formatting examples on rounding to 2 decimal places
        print("You ordered a {} {} for ${:.2f}".format(size,flavor,price))#I got :.2f from the link above
        # TODO: Remove the pass statement once you have your code written

    # TODO: Print the customer's total_bill
    print("Your total bill is: ${:.2f}".format(total_bill)) #this taken out of the loop is what will add the total bill together.
    # TODO: Once orders are all taken, the customer should be asked if they still want to Pay or Cancel
    #  "Would you like to pay or cancel the order (p/c)? "
    #   Hint: Use the get_first_letter_of_user_input() Re-prompt if answer does not start with 'p' or 'c'
    complete_payment = get_first_letter_of_user_input("Would you like to pay or cancel the order (p/c)? ")
    if complete_payment == 'p': #strip and lower method are provided already
        return total_bill
    elif complete_payment == 'c':
        return 0 #Im not returning the bill here.
    else:
        print("Please enter (p/c).")


def get_first_letter_of_user_input(question):
    """
    Takes in a string as its argument, to be used as the question you want the user to be asked.
    Gets input from the user, removes whitespace and makes all letters lowercase
    Hint: Use the strip() and lower() functions
    Returns: The first letter of the input the user provides. Ask again if the input is empty.
    """
    #You need a while loop here because if you don't enter a valid input, the input prompt won't reprompt.
    first_letter = ""
    # TODO: Write your code here

    while True: #needed to execute loop
        first_letter = (input(question).strip().lower())
        if first_letter:
            return first_letter[0] #here, I'm returning the first index that is provided by the user.
        if first_letter == "":
            print("Above is an empty input.")

def are_all_customers_served(customer_queue_length):
    """
    If there are no customers in the queue, returns True, and all customers have been served.
    Otherwise, returns False.
    Returns: True or False
    """
    # TODO: Write your code here
    #as each customer is served, once we get to 0, all customers will have then been served.
    if customer_queue_length == 0:
        return True
    else:
        return False


def print_current_status(customers_served, tracking_revenue):
    """
    Prints a message of how many customers have been served and the total sales of the ice cream stand.
    Hint: See https://www.w3schools.com/python/python_string_formatting.asp for string formatting examples on rounding to 2 decimal places
    No Return, only print statements
    """
    # TODO: Write your code here
    print("\nWe have now served {} customer(s), and received ${:.2f} in revenue\n".format(customers_served,tracking_revenue))
    # TODO: Remove the pass statement once you have your code written


def print_sales_summary(customers_served, tracking_revenue):
    """
    Takes in the arguments customers_served and tracking_revenue. Prints both
    arguments as strings to let the user know what those values are.
    Output should look something like:
        Total customers served: 3
        Total sales           : $xx.xx
    Hint: See https://www.w3schools.com/python/python_string_formatting.asp for string formatting examples on rounding to 2 decimal places
    No Return, only print statements
    """
    # TODO: Write your code here
    print("Total customers served: {}".format(customers_served))
    print("Total sales           : ${:.2f}".format(tracking_revenue))
    pass    # TODO: Remove the pass statement once you have your code written


def random_queue_length():
    """
    Takes no arguments.
    Uses the imported randint function to generate a random integer between 2 and 5 inclusive.
    Hint: See https://www.w3schools.com/python/ref_random_randint.asp
    Returns: The resulting random integer.
    """
    '''you don't need random.randint because randint was imported directly 
        from the import library. '''
    return randint(2,5) #thie will generate 2 to 5 people once we call it to our list of names


def main():
    """
    Lists of available flavors, sizes and prices. DO NOT CHANGE.
    For sizes and prices, we will use the following convention:
    Index 0 for Small
    Index 1 for Medium
    Index 2 for Large
    """
    ice_cream_flavors = ['Vanilla', 'Chocolate', 'Strawberry']
    ice_cream_sizes = ['Small', 'Medium', 'Large']
    ice_cream_prices = [4.99, 7.49, 8.49]


    #List of names of possible customers
    customer_names = ["Alice", "Bob", "Charlie", "Dan", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]

    program_running = True
    while program_running:
        # set shop to open
        input('Press any key to open the shop! ')
        queue_is_open = True
        # TODO: Call the print_welcome_and_menu function with the parameters in the following order -
        #  ice_cream_flavors, ice_cream_sizes, ice_cream_prices
        # This code isn't going to run until you define the three parameters. Once you do, the welcome message will print.
        print_welcome_and_menu(ice_cream_flavors, ice_cream_sizes, ice_cream_prices)

    # set initial values
        tracking_revenue = 0

        # will hold the list of names of the customers in the queue
        #here, customers in queue is being added to start a new list
        customers_in_queue = []
        customers_served = 0

        # TODO: Call the random_queue_length function and save the result to num_of_customers_in_queue
        num_of_customers_in_queue = random_queue_length()
        # TODO: Print how many customers are in the queue
        print("\nNum of customers in the queue: {}\n".format(num_of_customers_in_queue))

        # TODO: Call the imported choice function to generate a random name from customer_names.
        #   Then, append each name to the end of the customers_in_queue list.
        #   The total number of customer names added should be equal to num_of_customers_in_queue
        #   Hint: See https://www.w3schools.com/python/ref_random_choice.asp
        #   Note: It is OK to have duplicate names in the queue.
        while len(customers_in_queue) < num_of_customers_in_queue:
            name_chosen = random.choice(customer_names) #generates a random name from the customer name list
            #the line below essentially gets the name of the customers that were randomly chosen in queue. Only 2 to 5 will be selected.
            customers_in_queue.append(name_chosen)


        while queue_is_open:
            # TODO: Extract the first customer (index 0) from the customers_in_queue and save it to
            #  the current_customer_name variable.
            #  After extraction, the customer should now be removed from the customers_in_queue list.
            #  Hint: Use the pop function with an index argument
            '''For my learning purposes, originally you had:
                
                current_customer_name = customers_in_queue[0]
                current_customer_name.pop(0)
               
                The issue is though, when you go to call current_customer_name when taking the order,
                 the second line isn't even getting executed and your not actually removing the
                 first customer. '''

            if customers_in_queue:
                current_customer_name = customers_in_queue.pop(0)
            else:
                break

            # TODO: Take a customer at the window and update the revenue by calling the take_customer_order function
            #call current customer
            update_revenue = take_customer_order(current_customer_name, ice_cream_flavors, ice_cream_sizes, ice_cream_prices)
            tracking_revenue += update_revenue
            # TODO: Update the customers_served variable
            customers_served += 1 #customers served is set to 0.

            # TODO: Call the print_current_status
            print_current_status(customers_served, tracking_revenue)

            # TODO: Call the are_all_customers_served(customer_queue_length) function to check if there are any more
            #  customers in the queue.
            #  If False, continue the loop.
            #  If True, call the print_sales_summary(customers_served, tracking_revenue) and close the queue
            #I want the length of customers
            if are_all_customers_served(customers_in_queue):
                print_sales_summary(customers_served, tracking_revenue)
                queue_is_open = False
            #else:
             #   queue_is_open
            '''After running my code, the two lines above actually have no effect because 
                queue_is_open is already set to True so there is no point in the else statement here.'''

             # TODO: Remove the pass statement once you have your code written


        # TODO: Ask if you want to open the ice cream stand again "Do you want to open again (y/n)? "
        #  Hint: Use the get_first_letter_of_user_input function
        #  Update the program_running variable if you get a valid answer either 'y' or 'n'
        #  Otherwise, re-prompt until a valid answer is given'''
        #resume will run through the input of get first letter and allow the user to type
        while True:
            resume = get_first_letter_of_user_input("Do you want to open again (y/n)?")
            #strip and lower is already in the function
            if resume == "y":
                break #program running is already set to true
            elif resume == "n":
                program_running = False
                break
            else:
                print("Please enter (y/n).")

'''if you run this print(__name__), you will notice that the name of this module is 'main', not 'ice_cream_stand.py'.
    That's is because nothing is being imported so this module is running as the 'main' source code.'''

if __name__ == '__main__':
    main()
