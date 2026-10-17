import sys

tax_rate = 1.0825
tax = False
# user sees menu options for methods of price calculating or settings for adjusting calculations and other user setting
def print_menu():
    print("Select one of the following")
    print("1. Find price by totals")
    print("2. Find price by items")
    print("3. Change tax settings")
    print("4. Find price difference for a combo")
    print("5. Exit program")

def validate_num(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Please enter a valid number")

def print_settings():
    print("Select one of the following")
    print("1. Change tax rate")
    print("2. Toggle tax on/off")
    print("3. Exit settings")

def price_by_totals():
            incorrect_total = validate_num("Enter the original total: $")
            correct_total =  validate_num("Enter the desired total: $")
            total = incorrect_total - correct_total
            if tax: 
                total *= tax_rate
            return f"Refund amount: ${total:.2f}"

def price_by_items():
            items = []
            correct_total = 0
            continue_loop = True    
            while continue_loop == True:
                user_input = input("Press enter to break the loop, or enter the prices one by one: $")
                if user_input == "":
                    continue_loop = False
                else:
                    try:
                        items.append(float(user_input))
                    except ValueError:
                        print("Please enter a valid number")
            for item in items:
                correct_total += item
            incorrect_total = validate_num("Enter the original total: $")
            total = incorrect_total - correct_total
            if tax: 
                total *= tax_rate
            return f"Refund amount: ${total:.2f}"

def find_combo_price_difference():
    combo_price = validate_num("Enter the price of the desired combo: $")
    price_of_items = []
    for i in range(2):
        price_of_items.append(validate_num("Enter the price of the sandwich and drink/fry, one by one: $"))
    total = sum(price_of_items)
    return f"Price difference: ${abs(total - combo_price):.2f}"  


# we determine user input
def main_menu_selection():
    global tax
    global tax_rate
    main_menu_input = input("Enter 1, 2, 3, 4, or 5: ")
    result = None

# option 1: we take the incorrect total and desired total and find the difference
    if main_menu_input == "1":

        result = price_by_totals()
    
    elif main_menu_input == "2":

        result = price_by_items()
        
    elif main_menu_input == "3":
        print_settings()
        settings_input = input("Enter 1, 2, or 3: ")

        if settings_input == "1":
            tax_rate = validate_num("What would you like to change the tax to? Example: 1.0825\n")

        elif settings_input == "2":
            if tax == True:
                tax = False
                print("Tax has been toggled off")
            elif tax == False:
                tax = True  
                print("Tax has been toggled on")  

        elif settings_input == "3":
            result = None

        else:
            return "Please enter a valid number"

    elif main_menu_input == "4":
            result = find_combo_price_difference()

    elif main_menu_input == "5":
            sys.exit()

    else: 
        return "Please enter a valid number"  
        
    return result

# our running loop
while True:
    print_menu()
    result = main_menu_selection()
    if result == None:
        continue
    else:
        print(result)
