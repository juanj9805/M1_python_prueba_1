def string_input(noun):
    return input(f"Register {noun}: ")

def int_input(quantity):
    return int(input(f"Register {quantity}: "))

def float_input(price):
    return float(input(f"Register {price}: "))

def custom_input_value (data_type, noun):
    return data_type(input(f"Register {noun}"))