class VendingMachine:
    def __init__(self):
        # Initialize vending machine sections and items

        self.sections = {
            # Sections containing different categories of items

            '''
            \n\n
                        \033[94m                                           ・..----------------.  .----------------.  .----------------.  .-----------------. .----------------.  .----------------. ・.
                                             ✧                      ✧| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |               ✧
                                                               ゜ ・.| |  ________    | || |  _______     | || |     _____    | || | ____  _____  | || |  ___  ____   | || |    _______   | | .・゜
                                                          ✧       ・.| | |_   ___ `.  | || | |_   __ \    | || |    |_   _|   | || ||_   \|_   _| | || | |_  ||_  _|  | || |   /  ___  |  | |.・    ✧
                                                             -  ゜・.| |   | |   `. \ | || |   | |__) |   | || |      | |     | || |  |   \ | |   | || |   | |_/ /    | || |  |  (__ \_|  | |.・゜- 
                                                 ✧         .・      .| |   | |    | | | || |   |  __ /    | || |      | |     | || |  | |\ \| |   | || |   |  __'.    | || |   '.___`-.   | |.          ・.     ✧
                                                                 ・ .| |  _| |___.' / | || |  _| |  \ \_  | || |     _| |_    | || | _| |_\   |_  | || |  _| |  \ \_  | || |  |`\____) |  | |.・
                                                                    .| | |________.'  | || | |____| |___| | || |    |_____|   | || ||_____|\____| | || | |____||____| | || |  |_______.'  | |.
                                                                     | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
                                             . ・        ✧            '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'         ✧          ・.
''': {
                '                                                                                                          \033[97mSodas': {
                     # Items in the Sodas section
                     # Each item has a unique code, name, price, and quantity

                    '01': {'name': 'Coca-Cola', 'price': 1.50, 'quantity': 10},
                    '02': {'name': 'Pepsi', 'price': 1.25, 'quantity': 15},
                    '03': {'name': 'Sprite', 'price': 1.75, 'quantity': 12},
                    '04': {'name': 'Fanta', 'price': 1.75, 'quantity': 12},
                    '05': {'name': 'Dr. pepper', 'price': 1.75, 'quantity': 12},
                    '06': {'name': 'Gatorade', 'price': 1.75, 'quantity': 12},
                    '07': {'name': 'Canada Dry', 'price': 1.75, 'quantity': 12},
                    '08': {'name': 'Coke', 'price': 1.75, 'quantity': 12},
                    '09': {'name': 'A & W', 'price': 1.75, 'quantity': 12},
                    '10': {'name': 'Mountain Dew', 'price': 1.75, 'quantity': 12}
                },
                '                                                                                                          \033[97mBottled Water': {
                    # Items in the Bottled Water section
                    # Each item has a unique code, name, price, and quantity

                    '11': {'name': 'Dasani', 'price': 1.00, 'quantity': 20},
                    '12': {'name': 'Aquafina', 'price': 0.90, 'quantity': 25},
                    '13': {'name': 'Evian', 'price': 1.25, 'quantity': 18},
                    '14': {'name': 'Smart Water', 'price': 1.25, 'quantity': 18},
                    '15': {'name': 'Poland Spring', 'price': 1.25, 'quantity': 18},
                    '15': {'name': 'Perrier', 'price': 1.25, 'quantity': 18},
                    '16': {'name': 'Nestlé ', 'price': 1.25, 'quantity': 18},
                    '17': {'name': 'Voss', 'price': 1.25, 'quantity': 18},
                    '18': {'name': 'Fiji', 'price': 1.25, 'quantity': 18},
                    '19': {'name': 'Liquid Death', 'price': 1.25, 'quantity': 18},
                    '20': {'name': 'Waiakea', 'price': 1.25, 'quantity': 18}
                   
                },
                
            },
            '''
            \n\n
            \n\n
                               \033[93m                                      ・.----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------. 
                                              ✧                      ✧| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |・.
                                                                ゜ ・.| |    _______   | || | ____  _____  | || |      __      | || |     ______   | || |  ___  ____   | || |    _______   | |               ✧
                                                           ✧       ・.| |   /  ___  |  | || ||_   \|_   _| | || |     /  \     | || |   .' ___  |  | || | |_  ||_  _|  | || |   /  ___  |  | |.・゜
                                                              -  ゜・.| |  |  (__ \_|  | || |  |   \ | |   | || |    / /\ \    | || |  / .'   \_|  | || |   | |_/ /    | || |  |  (__ \_|  | |.・    ✧
                                                  ✧         .・      .| |   '.___`-.   | || |  | |\ \| |   | || |   / ____ \   | || |  | |         | || |   |  __'.    | || |   '.___`-.   | |.・゜- 
                                                                  ・ .| |  |`\____) |  | || | _| |_\   |_  | || | _/ /    \ \_ | || |  \ `.___.'\  | || |  _| |  \ \_  | || |  |`\____) |  | |.          ・.     ✧
                                                                     .| |  |_______.'  | || ||_____|\____| | || ||____|  |____|| || |   `._____.'  | || | |____||____| | || |  |_______.'  | |.・
                                                            .  ・  ゜ | |              | || |              | || |              | || |              | || |              | || |              | |゜・.
                                                                      | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
                                              . ・        ✧            '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'          ✧          ・.
''': {
                '                                                                                                          \033[97mChips': {
                     # Items in the chips section
                     # Each item has a unique code, name, price, and quantity

                    '20': {'name': 'Potato Chips', 'price': 1.25, 'quantity': 20},
                    '21': {'name': 'Tortilla Chips', 'price': 1.50, 'quantity': 15},
                    '22': {'name': 'Pretzels', 'price': 1.00, 'quantity': 18},
                    '23': {'name': 'TGI Fridays', 'price': 1.25, 'quantity': 20},
                    '24': {'name': 'Takis', 'price': 1.25, 'quantity': 20},
                    '25': {'name': 'Funyuns', 'price': 1.25, 'quantity': 20},
                    '26': {'name': 'Cheetos', 'price': 1.25, 'quantity': 20},
                    '27': {'name': 'Pringles', 'price': 1.25, 'quantity': 20},
                    '28': {'name': 'Fritos', 'price': 1.25, 'quantity': 20},
                    '29': {'name': 'Lays', 'price': 1.25, 'quantity': 20},
                    '30': {'name': 'Doritos', 'price': 1.25, 'quantity': 20}
                    
                },
                '                                                                                                          \033[97mCandy': {
                     # Items in the candy section
                     # Each item has a unique code, name, price, and quantity

                    '31': {'name': 'Chocolate Bar', 'price': 1.75, 'quantity': 12},
                    '32': {'name': 'Gummy Bears', 'price': 1.00, 'quantity': 25},
                    '33': {'name': 'Lollipops', 'price': 0.75, 'quantity': 20},
                    '34': {'name': 'Snickers', 'price': 1.25, 'quantity': 20},
                    '35': {'name': 'Kit Kat', 'price': 1.25, 'quantity': 20},
                    '36': {'name': 'Twix', 'price': 1.25, 'quantity': 20},
                    '37': {'name': 'Reeses ', 'price': 1.25, 'quantity': 20},
                    '38': {'name': 'Milky Way', 'price': 1.25, 'quantity': 20},
                    '39': {'name': 'M&Ms', 'price': 1.25, 'quantity': 20},
                    '40': {'name': 'Sour Patch', 'price': 1.25, 'quantity': 20},

                    
                },
                
            },

            }
        

    def display_items(self):
        print("\n")
        print("\n")
        print("\n")
        print("                                              ∘₊✧.───────────────────────────────────────────────────────────.·:*¨༺                        ༻¨*:·.────────────────────────────────────────────────────────────────.✧₊∘")
        print("\n")
        print("\033[97m                                                                                    ✧                                                                                                                         ✧")
        print("                                                       .・゜゜｡･ﾟﾟ･・  ██╗   ██╗███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗     ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗  ・゜゜･ﾟﾟ･｡・．")
        print("                                              .・゜-: ✧ :-*:･ﾟ✧*:･ﾟ✧   ██║   ██║██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝     ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝ ✧･ﾟ: *✧･ﾟ:* -: ✧ :-.・．")
        print("                                              *✧･ﾟ: *✧･ﾟ:*✧･ﾟ: *✧･ﾟ:   ██║   ██║█████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗    ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  ✧･ﾟ: *✧･ﾟ:*✧･ﾟ: *✧･ﾟ:")
        print("                                              .・゜-: ✧ :-*:･ﾟ✧*:      ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║    ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  .✧･ﾟ: *✧･ﾟ:* -: ✧ :-.・．")
        print("                                                         : ✧ :-*:･ﾟ✧*:  ╚████╔╝ ███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗‧̍̊: ✧ :-*:･ﾟ✧*:  ")
        print("\n")
        print("                                             ∘₊✧.───────────────────────────────────────────────────────────────.·:*¨༺                   ༻¨*:·.──────────────────────────────────────────────────────────────────.✧₊∘")
        
        # Display items available in the vending machine.
        # Prints the items in a formatted way for each section and category.

        for section, categories in self.sections.items():
            print(f"\n{section}:")
            for category, items in categories.items():
                print(f"                                                                                                          \n{category}:")
                print("                                                                                                          +" + "-"*41 + "+")
                print("                                                                                                          | Code |   Item        |  Price  | Stock  |")
                print("                                                                                                          +" + "-"*41 + "+")
                for key, item in items.items():
                    spaces = " " * (14 - len(item['name']))
                    stock_status = "Out of Stock" if item['quantity'] == 0 else str(item['quantity'])
                    print(f"                                                                                                          |  {key}  | {item['name']}{spaces}|  ${item['price']:<6.2f}| {stock_status:^5}  |")
                print("                                                                                                          +" + "-"*41 + "+")

    def purchase_item(self, item_code, quantity, amount):

        # Allow purchasing an item by specifying item code, quantity, and amount
        # Checks if the item is available and if the provided amount is sufficient

        for section, categories in self.sections.items():
            for category, items in categories.items():
                if item_code in items:
                    item = items[item_code]
                    if item['quantity'] >= quantity and amount >= (item['price'] * quantity):
                        if quantity <= item['quantity']:
                            item['quantity'] -= quantity
                            total_price = item['price'] * quantity
                            change = amount - total_price
                            print("                                                                                                          +" + "-"*52 + "+")
                            print(f"                                                                                                          | You've purchased {quantity} {item['name']}.{' '*(12 - len(str(quantity)))}|")
                            print(f"                                                                                                          | Your change: ${change:.2f}{' '*(17-len(str(change)))}|")
                            print("                                                                                                          +" + "-"*52 + "+")
                            return
                        else:
                            print("                                                                                                          +" + "-"*52 + "+")
                            print("                                                                                                          | Insufficient quantity available.{' '*(7)}|")
                            print("                                                                                                          +" + "-"*52 + "+")
                            return
                    else:
                        print("                                                                                                          +" + "-"*52 + "+")
                        print("                                                                                                          | Insufficient quantity or funds.{' '*(10-len('Insufficient quantity or funds.'))}|")
                        print("                                                                                                          +" + "-"*52 + "+")
                        return

        print("                                                                                                          +" + "-"*52 + "+")
        print("                                                                                                          | Invalid item code.{' '*(17-len('Invalid item code.'))}|")
        print("                                                                                                          +" + "-"*52 + "+")


def main():

    # Create a VendingMachine instance.

    vending_machine = VendingMachine()

    while True:
        vending_machine.display_items() # Ask user for item code

        item_code = input("                                                                                                          Enter the item code (q to quit): ")

        quantity = int(input("                                                                                                          Enter the quantity: "))
        amount = float(input("                                                                                                          Enter the amount: "))

        vending_machine.purchase_item(item_code, quantity, amount)

def main():
    vending_machine = VendingMachine()

    while True:
        vending_machine.display_items()

        item_code = input("                                                                                                          Enter the item code : ")
        
        # Ask user for quantity
        quantity = int(input("                                                                                                          Enter the quantity: "))
        
        # Ask user for amount paid
        amount = float(input("                                                                                                          Enter the amount: "))

        vending_machine.purchase_item(item_code, quantity, amount)

        choice = input("                                                                                                          Would you like to buy anything else? (yes/no): ")
        if choice.lower() != 'yes':
            break

# Run the main vending machine interaction loop
if __name__ == "__main__":
    main()