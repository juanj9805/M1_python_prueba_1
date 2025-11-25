from helpers import principal_menu, date_generator, ID_generator, string_input, int_input, float_input
import datetime

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

# Inventory managament

def register_product (products_list):
    product_info = {
                "book_ID" : ID_generator(),
                "book_title" : string_input("book title"),
                "book_author" : string_input("book author"),
                "book_category" : string_input("book category"),
                "book_price" : string_input("book price"),
                "book_stock" : string_input("book stock"),
            }
    products_list.append(product_info)

def show_products_inventory (products_list):
    print(f"Inventory stock:\n{products_list}")

def search_product_by_name (products_list):
    search_book = string_input("product to search by name: ")
    for product in products_list:
        if search_book == product["book_title"]:
            print(f"Product found:\n{product}")
            return product

def search_product_by_ID (products_list):
    search_book = string_input("Register the ID: ")
    for product in products_list:
        if search_book == product["book_ID"]:
            print(f"Product found:\n{product}")
            return product

def update_product (products_list):
    product_to_update = search_product_by_name(products_list)
    for product in products_list:
        print(product)
        if product_to_update["book_title"] == product["book_title"]:
            new_name = string_input("new name: ")
            product["book_title"] = new_name
            return product

def delete_product (products_list):
    product_to_delete = search_product_by_name(products_list)
    for product in products_list:
        if product_to_delete["book_title"] == product["book_title"]:
            products_list.remove(product)
            print(f"THe next product was deleted from the books list:\n{product}")
    return product

# Sales management

def register_sale (sales_list,products_list):
    product_to_sale = search_product_by_name(products_list)
    product_quantity = int_input("quantity product")
    total_price = product_quantity * product_to_sale["book_price"]
    if product_to_sale["book_stock"] < product_quantity:
        return print(f"{product_to_sale["book_title"]} stock insuficient, there are just {product_to_sale["book_stock"]} books of them")
    
    sale_info = {
                "sale_ID" : ID_generator(),
                "user_ID" : string_input("user id"),
                "ID_book" : product_to_sale["book_ID"],
                "quantity_product" : product_quantity,
                "date" : date_generator(),
                # "discount" : float_input("discount"),
                "total_price" : total_price, 
            }
    product_to_sale["book_stock"] -= product_quantity
    sales_list.append(sale_info)
    return sale_info

def show_sales (sales_list):
    print(f"Sales information:\n{sales_list}")

# Reports management

def products_best_seller (sales_list):
    best_seller = {}
    for sale in sales_list:
        best_sell = 0
        if sale["total_price"] > best_sell:
            best_sell += sale["total_price"]
            best_seller = {
            "ID_best_seller" : sale["ID_book"],
            "total_price" : sale["total_price"]
            }
    return best_seller

def products_major_sales_by_author (sales_list):
    best_sell = products_best_seller(sales_list)
    book_info = search_product_by_ID(books,best_sell["ID_best_seller"])
    author_seller = book_info["book_author"]
    return author_seller

def products_raw_income (sales_list):
    raw_income = 0
    for sale in sales_list:
        raw_income += sale["total_price"]
    return raw_income

def products_net_income (sales_list):
    net_income = products_raw_income(sales_list)
    net_income -=  (operation_cost * net_income) + (net_income * TAX)
    return net_income

# 4. Validaciones avanzadas
# • Validar entradas (números positivos, formatos correctos, campos obligatorios).
