CUSTOMERS = [
    {
        "email": "jas@jas.com",
        "password": "jas",
        "name": "Jas Kas",
        "id": 1
    },
    {
        "email": "beef@beef.com",
        "password": "beef",
        "name": "Beef Lasagna",
        "id": 2
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