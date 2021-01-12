EMPLOYEES = [
    {
        "name": "Sam",
        "locationId": 1,
        "animalId": 1,
        "id": 1
    },
    {
        "name": "Sindy",
        "locationId": 2,
        "animalId": 4,
        "id": 2
    },
    {
        "name": "Vincent",
        "locationId": 1,
        "animalId": 3,
        "id": 3
    }
]

def get_all_employees():
    return EMPLOYEES


def get_single_employee(id):    
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee