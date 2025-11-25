import uuid
import datetime

def principal_menu ():
    return int(input(
    "Choose one module\n"
    "1- Inventory\n"
    "2- Sales\n"
    "3- Reports\n"
    "4- Exit\n"
    ))

def inventory_management_menu ():
    return int(input(
    "Choose one option\n"
    "1- Register product\n"
    "2- Search product\n"
    "3- Update product\n"
    "4- Delete product\n"
    "5- Exit\n"
    ))

def sales_management_menu ():
    return int(input(
    "Choose one option\n"
    "1- Register sale\n"
    "2- Show sales\n"
    "3- Exit\n"
    ))

def report_management_menu ():
    return int(input(
    "Choose one option to watch reports\n"
    "1- Best seller\n"
    "2- Major sales by author\n"
    "3- Raw income\n"
    "4- Net income\n"
    "5- Exit\n"
    ))

def options_menu ():
    return int(input(
    "Choose one option\n"
    "1- Show whole inventory:\n"
    "2- Show product info by name:\n"
    "3- Show product info by ID:\n"
    "4- Exit:\n"
    ))

def date_generator ():
    return str(datetime.datetime.now())

def ID_generator ():
    return str(uuid.uuid4())

def custom_input_value (data_type, noun):
    return data_type(input(f"Register {noun}"))

# def string_input(noun):
#     return input(f"Register {noun}: ")

# def int_input(quantity):
#     return int(input(f"Register {quantity}: "))

# def float_input(price):
#     return float(input(f"Register {price}: "))

