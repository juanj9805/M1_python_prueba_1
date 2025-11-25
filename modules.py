from services import register_product, show_products_inventory, search_product_by_name, search_product_by_ID, update_product, delete_product, register_sale, show_sales, products_best_seller, products_major_sales_by_author, products_raw_income, products_net_income
from helpers import   options_menu, inventory_management_menu, sales_management_menu, report_management_menu

def inventory_management_module (products_list):
    follow = True
    while follow:
        follow_option = True
        inventory_management_choice = inventory_management_menu()
        if inventory_management_choice == 1:
            register_product(products_list)
        elif inventory_management_choice == 2:
            while follow_option:
                choice = options_menu()
                print(choice)
                if choice == 1:
                    show_products_inventory(products_list)
                elif choice == 2:
                    search_product_by_name(products_list)
                elif choice == 3:
                    search_product_by_ID(products_list)
                elif choice == 4:
                    follow_option = False
        elif inventory_management_choice == 3:
            update_product(products_list)
        elif inventory_management_choice == 4:
            delete_product(products_list)
        elif inventory_management_choice == 5:
            follow = False

def sales_management_module (sales_list, products_list):
    follow = True
    while follow:
        sales_management_choice = sales_management_menu()
        if sales_management_choice == 1:
            register_sale(sales_list, products_list)
        elif sales_management_choice == 2:
            show_sales(sales_list)
        elif sales_management_choice == 3:
            follow = False

def reports_management_module (sales_list):
    follow = True
    while follow:
        reports_management_choice = report_management_menu()
        if reports_management_choice == 1:
            print(products_best_seller(sales_list))
        elif reports_management_choice == 2:
            print(products_major_sales_by_author(sales_list))
        elif reports_management_choice == 3:
            print(products_raw_income(sales_list))
        elif reports_management_choice == 4:
            print(products_net_income(sales_list))
        elif reports_management_choice == 5:
            follow = False