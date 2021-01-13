CUSTOMERS = [
    {
        "id": 1,
        "email": "jas@jas.com",
        "password": "jas",
        "name": "Jas Kas"
    },
    {
        "id": 2,
        "email": "beef@beef.com",
        "password": "beef",
        "name": "Beef Lasagna"
    }
]

def get_all_customers():
    return CUSTOMERS


def get_single_customer(id):    
    requested_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    return requested_customer

def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    # Return the dictionary with `id` property added
    return customer

def delete_customer(id):
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break