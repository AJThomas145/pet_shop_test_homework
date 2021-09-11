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

def get_pets_by_breed(users, breed):
    number_in_breed = [] 
    for dog in users["pets"]:
        if dog["breed"] == breed:
            number_in_breed.append(dog)
    return number_in_breed