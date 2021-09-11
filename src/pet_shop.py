import pdb
def get_pet_shop_name(user):
    return user["name"]

def get_total_cash(user):
    return user["admin"]["total_cash"]

def add_or_remove_cash(user, amount):
    user["admin"]["total_cash"] += amount

def get_pets_sold(user):
    return user["admin"]["pets_sold"]

def increase_pets_sold(user, new_sales):
    user["admin"]["pets_sold"] += new_sales

def get_stock_count(user):
    return len(user["pets"])

def get_pets_by_breed(user, breed):
    number_in_breed = [] 
    for dog in user["pets"]:
        if dog["breed"] == breed:
            number_in_breed.append(dog)
    return number_in_breed

def find_pet_by_name(user, name):
    for dog in user["pets"]:
        if dog["name"] == name:
            return dog

def remove_pet_by_name(user, remove_pet):
    pet_to_delete = None
    for dog in user["pets"]:
        if dog["name"] == remove_pet:
            pet_to_delete = dog
            break

    user["pets"].remove(pet_to_delete)

def add_pet_to_stock(user, new_pet):
    user["pets"].append(new_pet)

def get_customer_cash(user):
    return user["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(customer):
     return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    return customer["pets"].append(pet)
    