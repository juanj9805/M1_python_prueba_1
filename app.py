from helpers import principal_menu
from modules import inventory_management_module, sales_management_module, reports_management_module

def app ():
    books = [
    {'book_ID': '7ce5438a-8cd7-42af-af8d-240bbf619518', 'book_title': 'the prince', 'book_author': 'nicolas machiavelo', 'book_category': 'politics', 'book_price': 80000, 'book_stock': 30},
    {'book_ID': '995522c8-bad2-410f-898c-c165b08b48aa', 'book_title': 'clean code', 'book_author': 'bob martin', 'book_category': 'software', 'book_price': 180000, 'book_stock': 15},
    {'book_ID': '2a819753-01a5-4bc9-ad16-1c4fdf986803', 'book_title': 'bible', 'book_author': 'pedro', 'book_category': 'religion', 'book_price': 110000, 'book_stock': 33},
    {'book_ID': '57a0a28b-6a28-4571-a84c-b961f9fc7a46', 'book_title': 'data structures and algorithms', 'book_author': 'susan cooper', 'book_category': 'software', 'book_price': 70000, 'book_stock': 12},
    {'book_ID': 'eedd9c37-8504-443a-8461-2e33089f7b0f', 'book_title': 'atomic habits', 'book_author': 'juan', 'book_category': 'wellness', 'book_price': 95000, 'book_stock': 3}
    ]

    sales = [
    {'sale_ID': '8db297b1-c857-4aac-a5bf-1f2673b8de50', 'user_ID': '23', 'ID_book': '2a819753-01a5-4bc9-ad16-1c4fdf986803', 'quantity_product': 3, 'date': '2025-11-24 18:26:37.152528', 'total_price': 330000},
    {'sale_ID': '8db297b1-c857-4aac-a5bf-1f2673b8de51', 'user_ID': '32', 'ID_book': '2a819753-01a5-4bc9-ad16-1c4fdf986803', 'quantity_product': 2, 'date': '2025-11-24 18:26:37.152528', 'total_price': 220000},
    {'sale_ID': '8db297b1-c857-4aac-a5bf-1f2673b8de52', 'user_ID': '1', 'ID_book': '995522c8-bad2-410f-898c-c165b08b48aa', 'quantity_product': 2, 'date': '2025-11-24 18:26:37.152528', 'total_price': 360000},
    ]

    TAX = 0.17
    operation_cost = 0.33

    follow = True
    while follow:
        principal_choice = principal_menu()
        if principal_choice == 1:    
            inventory_management_module(books)
        elif principal_choice == 2:
            sales_management_module(sales,books)
        elif principal_choice == 3:    
            reports_management_module(sales)
        elif principal_choice == 4:
            follow = False

app()



