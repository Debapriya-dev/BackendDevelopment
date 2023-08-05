employee_list = [{"id": 12345, "name": "John", "department": "Kitchen"}, {"id": 12458, "name": "Paul", "department": "House Floor"}]

def get_employee(id): 
    for employee in employee_list:
        if employee['id'] == id:
            return employee

print(get_employee(12458));
## OUTPUT
#{'id': 12458, 'name': 'Paul', 'department': 'House Floor'}

employee_dict = {
    123456 : {
        "id" : "12345",
        "name" : "DB",
        "dept" : "Kitchen"
    },
    1234678: {
        "id" : "1234678",
        "name" : "JD",
        "dept" : "Retail"
    }
}
def get_employeef_from_dict(id):
    # if(employee_dict[id] == null):
    #     print("No e,ployee exists with this id")
    return employee_dict[id]

print(get_employeef_from_dict(123456))