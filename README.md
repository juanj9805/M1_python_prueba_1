## DESCRIPTION

Based on the guide I start to identify some patterns that let me see that a bunch of code it was been repited along all the code and some functios have a strong relation among them, such as information about products, information about sales, and information about reports, based on this hypotesis I took the decision to work on each one using something called atomic design, where we have atoms(functios stored inside helpers folder), molecules(functions stored inside, services folder), organism(functions stored inside modules folder) and templates(main app) and with the union of all this concepts by imports and exports inside the code the main app works seamless

## STEP BY STEP

I create 4 folders:

- helpers
- services
- modules
- app

### helpers.py

In this folder I am using the functions that are been repeting along all the code, all modules do imports from it due to the amount of times code is repited or similar

- principal_menu: This is used in the app and here is all starts
- date_generator: This is used to generate information about the current date of each sale
- ID_generator: Used to generate uuid ids
- string_input: This is specially created to stored information about each input catalogued as string
- int_input: This is specially created to stored information about each input catalogued as integer
- float_input: This is specially created to stored information about each input catalogued as float, use wit all the prices on the app

### services.py

Here I am using the functions I considered are features, and I am wrapping all the logic of this services in something bigger called modules

#### Product

- register_product: create product info and store it in a dictionarie. later this dictionarie is included in a list using append method
- show_products_inventory: Do a print of the whole product list or a product by ID or name
- search_product_by_name: Seek a product by its name
- search_product_by_ID: Seek a product by its ID
- update_product: Use search_product_by_name() function to found the product and then update it
- delete_product: Use search_product_by_name() function to found the product and then delete it

#### Sales

- register_sale: This was one of the most challenging due to It was neccesary to manipulate from differents sources
- show_sales: Show all the sales list

#### Reports

- products_best_seller: Based on the information of each sale stored inside a dictionarie take its total price and show it
- products_major_sales_by_author: Another callenging part, due to I have to mix returns from 3 functions to show just the name of the author
- products_raw_income: It was too easy, due to I just need to figure out the value of all the sales and add each one
- products_net_income: With the information gathered in raw income I just do a deductions using a const TAX and variable operations_cost

### modules.py

Based on the guide I identify group of functions that later I gonna use as modules.
These functions are the bigest and each of them is wrapping a group of services that have a strong relationship among them.
For example: (all services realtioned with books are a inventory management), (Services relatio)

### app.py

Where the magic happens, here I am usign the modules each one of them has a services and each services has helpers including the app,

- inventory_management_module: All functions relationed with product are running here
- sales_management_module: All functions relationed with sales are running here
- reports_management_module: All functions relationed with reports are running here

## Data storage

### Products information

dict_keys([
'book_ID': Used to manipulate data with this
'book_title':
'book_author':
'book_category':
'book_price':
'book_stock':
])

### Sales information

dict_keys[
'sale_ID': Used to manipulate data with this
'user_ID': Used to manipulate data with this
'ID_book': Used to manipulate data with this
Here all the IDS were used thinking to create relationships due to is the way used to handle data in real life, I took the decision to create something called (normalizacion de base de datos)
And With these IDS then I create relation, and if I need to get the information about each product I just seek it by its ID
'quantity_product':
'date':
'total_price'
]:

# M1_python_prueba_1
