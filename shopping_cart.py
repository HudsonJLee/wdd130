# Shopping Cart Program
# Author: Hudson Lee
#
# Creativity additions: Each item stores a quantity in addition to a name and price,
# so the user can add multiple units of the same item at once. The cart display
# shows quantity, unit price, and a line total (qty × price), and the total
# reflects quantities as well.

# ── Cart storage ──────────────────────────────────────────────────────────────
names = []
prices = []
quantities = []


# ── Helpers ───────────────────────────────────────────────────────────────────

def display_cart():
    """Print every item with its number, quantity, unit price, and line total."""
    if not names:
        print("Your cart is empty.")
        return
    print("The contents of the shopping cart are:")
    for i in range(len(names)):
        line_total = prices[i] * quantities[i]
        qty_label = f"x{quantities[i]}" if quantities[i] > 1 else "   "
        print(f"  {i + 1}. {names[i]:<20} {qty_label}  ${prices[i]:.2f}  (${line_total:.2f})")


# ── Menu actions ──────────────────────────────────────────────────────────────

def add_item():
    name = input("What item would you like to add? ").strip()
    price_input = input(f"What is the price of '{name}'? ").strip()
    try:
        price = float(price_input)
    except ValueError:
        print("Invalid price. Item not added.")
        return
    qty_input = input(f"How many '{name}'? (press Enter for 1) ").strip()
    if qty_input == "":
        qty = 1
    else:
        try:
            qty = int(qty_input)
            if qty < 1:
                raise ValueError
        except ValueError:
            print("Invalid quantity. Item not added.")
            return
    names.append(name)
    prices.append(price)
    quantities.append(qty)
    print(f"'{name}' has been added to the cart.")


def remove_item():
    display_cart()
    if not names:
        return
    choice = input("\nWhich item would you like to remove? ").strip()
    try:
        index = int(choice) - 1
    except ValueError:
        print("Sorry, that is not a valid item number.")
        return
    if index < 0 or index >= len(names):
        print("Sorry, that is not a valid item number.")
        return
    removed = names[index]
    names.pop(index)
    prices.pop(index)
    quantities.pop(index)
    print(f"'{removed}' has been removed.")


def compute_total():
    if not names:
        print("Your cart is empty.")
        return
    total = sum(prices[i] * quantities[i] for i in range(len(names)))
    print(f"The total price of the items in the shopping cart is ${total:.2f}")


# ── Main loop ─────────────────────────────────────────────────────────────────

print("Welcome to the Shopping Cart Program!")

while True:
    print()
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    action = input("Please enter an action: ").strip()

    if action == "1":
        add_item()
    elif action == "2":
        display_cart()
    elif action == "3":
        remove_item()
    elif action == "4":
        compute_total()
    elif action == "5":
        print("Thank you. Goodbye.")
        break
    else:
        print("Invalid option. Please enter a number from 1 to 5.")
