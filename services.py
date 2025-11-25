from helpers import  date_generator, ID_generator, custom_input_value

# Inventory managament

def register_product (products_list):
        product_info = {
                    "book_ID" : ID_generator(),
                    "book_title" : custom_input_value(str,"Book title: "),
                    "book_author" : custom_input_value(str,"Book author: "),
                    "book_category" : custom_input_value(str,"Book category: "),
                    "book_price" : custom_input_value(float,"Book price: "),
                    "book_stock" : custom_input_value(int,"Book stock: "),
                }
        products_list.append(product_info)

def show_products_inventory (products_list):
    print(f"Inventory stock:\n{products_list}")

def search_product_by_name (products_list):
    search_book = custom_input_value(str,"product to search by book title: ")
    for product in products_list:
        if search_book == product["book_title"]:
            print(f"Product found:\n{product}")
            return product

def search_product_by_ID (products_list):
    search_book = custom_input_value(str,"Register the Book ID: ")
    for product in products_list:
        if search_book == product["book_ID"]:
            print(f"Product found:\n{product}")
            return product

def update_product (products_list):
    product_to_update = search_product_by_name(products_list)
    for product in products_list:
        print(product)
        if product_to_update["book_title"] == product["book_title"]:
            new_name = custom_input_value(str,"New title for this book: ")
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
    product_quantity = custom_input_value(int,"Enter the product quantity to sell: ")
    total_price = product_quantity * product_to_sale["book_price"]
    if product_to_sale["book_stock"] < product_quantity:
        return print(f'{product_to_sale["book_title"]} stock insuficient, there are just {product_to_sale["book_stock"]} books of them')
    
    sale_info = {
                "sale_ID" : ID_generator(),
                "user_ID" : custom_input_value(str,"Enter user ID: "),
                "ID_book" : product_to_sale["book_ID"],
                "quantity_product" : product_quantity,
                "date" : date_generator(),
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
    print(best_sell)
    book_info = search_product_by_ID(products_list)
    print(book_info)
    author_seller = book_info["book_author"]
    return author_seller

def products_raw_income (sales_list):
    raw_income = 0
    for sale in sales_list:
        raw_income += sale["total_price"]
    return raw_income

def products_net_income (sales_list):
    TAX = 0.17
    operation_cost = 0.33
    net_income = products_raw_income(sales_list)
    net_income -=  (operation_cost * net_income) + (net_income * TAX)
    return net_income