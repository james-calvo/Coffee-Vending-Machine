def display_products(products):
    print("Available products:")
    for product, details in products.items():
        print(f"{product}: {details['sizes']}")

def select_product(products):
    while True:
        choice = input("Enter the name of the product you want to purchase: ")
        if choice in products:
            return choice
        else:
            print("Invalid product name. Please try again.")

def select_size(product_details):
    available_sizes = product_details['sizes']
    while True:
        choice = input("Select size (short, tall, grande): ").lower()
        if choice in ['short', 'tall', 'grande']:
            return choice
        else:
            print("Invalid size. Please select from available sizes.")


def insert_money():
    while True:
        try:
            money = float(input("Enter the amount of money you want to insert: ₱"))
            if money >= 0:
                return money
            else:
                print("Invalid amount. Please enter a non-negative value.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def vending_machine():
    products = {
        "Caramel Macchiato": {
            "short": 150.50,
            "tall": 180.00,
            "grande": 210.00,
            "sizes": ["short - ₱150.50", "tall - ₱180.00", "grande - ₱210.00"]
        },
        "Vanilla Latte": {
            "short": 135.00,
            "tall": 155.00,
            "grande": 180.00,
            "sizes": ["short - ₱135.00", "tall - ₱155.00", "grande - ₱180.00"]
        },
        "Mocha": {
            "short": 120.00,
            "tall": 140.00,
            "grande": 160.00,
            "sizes": ["short - ₱120.00", "tall - ₱140.00", "grande - ₱160.00"]
        },
        "Hazelnut Coffee": {
            "short": 120.00,
            "tall": 140.00,
            "grande": 160.00,
            "sizes": ["short - ₱120.00", "tall - ₱140.00", "grande - ₱160.00"]
        },
        "Cinnamon Spice Coffee": {
            "short": 145.00,
            "tall": 165.00,
            "grande": 190.00,
            "sizes": ["short - ₱145.00", "tall - ₱165.00", "grande - ₱190.00"]
        }
    }

    display_products(products)
    selected_product = select_product(products)
    product_details = products[selected_product]

    print(f"The available sizes and prices for {selected_product}:")
    for size in product_details['sizes']:
        print(size)

    selected_size = select_size(product_details)
    product_price = product_details[selected_size]

    print(f"The price of {selected_size} {selected_product} is ₱{product_price}")

    while True:
        money_inserted = insert_money()
        if money_inserted >= product_price:
            change = money_inserted - product_price
            print(f"Dispensing {selected_size} {selected_product}...")
            if change > 0:
                print(f"Your change: ₱{change}")
            break
        else:
            print("Insufficient funds. Please insert more money.")

vending_machine()
