import sys

from calculator import combo_upgrade_cost, refund_by_items, refund_by_totals

tax_rate = 1.0825
tax = False


# user sees menu options for methods of price calculating or settings for adjusting calculations and other user setting
def print_menu():
    print("Select one of the following")
    print("1. Find price by totals")
    print("2. Find price by items")
    print("3. Change tax settings")
    print("4. Find combo upgrade cost")
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
    original = validate_num("Enter the original total: $")
    desired = validate_num("Enter the desired total: $")
    refund = refund_by_totals(original, desired, tax, tax_rate)
    return f"Refund amount: ${refund:.2f}"


def price_by_items():
    items = []
    continue_loop = True
    while continue_loop:
        user_input = input(
            "Press enter to break the loop, or enter the prices one by one: $"
        )
        if user_input == "":
            continue_loop = False
        else:
            try:
                items.append(float(user_input))
            except ValueError:
                print("Please enter a valid number")
    original = validate_num("Enter the original total: $")
    refund = refund_by_items(items, original, tax, tax_rate)
    return f"Refund amount: ${refund:.2f}"


def find_combo_upgrade_cost():
    combo_price = validate_num("Enter the price of the desired combo: $")
    sandwich = validate_num("Enter the price of the sandwich: $")
    side = validate_num("Enter the price of the side: $")
    cost = combo_upgrade_cost(combo_price, sandwich, side)
    return f"Upgrade cost: ${cost:.2f}"


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
            tax_rate = validate_num(
                "What would you like to change the tax to? Example: 1.0825\n"
            )

        elif settings_input == "2":
            tax = not tax
            print(f"Tax is now {'on' if tax else 'off'}")

        elif settings_input == "3":
            result = None

        else:
            return "Please enter a valid number"

    elif main_menu_input == "4":
        result = find_combo_upgrade_cost()

    elif main_menu_input == "5":
        sys.exit()

    else:
        return "Please enter a valid number"

    return result


# our running loop
def main():
    while True:
        print_menu()
        result = main_menu_selection()
        if result is not None:
            print(result)

if __name__ == "__main__":
    main()