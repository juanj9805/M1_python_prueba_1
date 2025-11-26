from modules import inventory_management_module, sales_management_module, reports_management_module
from helpers import principal_menu
from data import books, sales

def app ():
    follow = True
    while follow:
        try:
            principal_choice = principal_menu()
            if principal_choice == 1:    
                inventory_management_module(books)
            elif principal_choice == 2:
                sales_management_module(sales,books)
            elif principal_choice == 3:    
                reports_management_module(sales,books)
            elif principal_choice == 4:
                follow = False
        except ValueError:
            print("\nPlease enter a valid number.")

app()