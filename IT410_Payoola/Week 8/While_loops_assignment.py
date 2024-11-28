employee_numbers = [1121, 1122, 1127, 1132, 1137, 1138, 1152, 1157]
employee_names = [
    "Jackie Grainger", "Jignesh Thrakkar", "Dion Green", 
    "Jacob Gerber", "Sarah Sanderson", "Brandon Heck", 
    "David Toma", "Charles King"]

employee_salaries = [22.22, 25.25, 28.75, 24.32, 23.45, 25.84, 22.65, 23.75]
total_hourly_rate = [28.886, 32.825, 37.375, 31.616, 30.485, 33.582, 29.445, 30.875]
company_raises = [23.32, 26.31, 29.61, 25.14, 24.18, 26.40, 23.10, 24.20]


employee_records = []


for i in range(len(employee_numbers)):
    employee_id = employee_numbers[i]
    employee_name = employee_names[i]

    if isinstance(employee_id, int) and 0 <= employee_id < 10**7:

     
        employee_record = {"employee_id": employee_id,
            "name": employee_names[i],
            "salary": employee_salaries[i],
            "total_hourly_rate": total_hourly_rate[i],
            "new_hourly_rate": company_raises[i]}
        
        employee_records.append(employee_record)
    else:
        print("Invalid Employee ID:", employee_id, "must be a number with 7 or fewer digits.")

#print final list of employee records
print("employee records:")
for record in employee_records:
    print(record)

#assignment 

import re

def is_valid_employee_id(emp_id):
    return isinstance(emp_id, int) and 0 <= emp_id < 10**7

def is_valid_name(name):
    return bool(re.match("^[a-zA-Z ]+$", name))

def is_valid_email(email):
    return bool(re.match("^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$", email))

def is_valid_address(address):
    if address == "":
        return True 
    return bool(re.match("^[a-zA-Z0-9 ]+$", address))

def get_employee_info():
    while True:
        emp_id = input("Enter Employee ID (7 digits or less): ")
        if not emp_id.isdigit() or not is_valid_employee_id(int(emp_id)):
            print("Invalid Employee ID. Must be a number with 7 or fewer digits.")
            continue
        
        emp_name = input("Enter Employee Name: ")
        if not is_valid_name(emp_name):
            print("Invalid Employee Name. Must contain only letters and spaces.")
            continue

        emp_email = input("Enter Employee Email Address: ")
        if not is_valid_email(emp_email):
            print("Invalid Email Address. Must be in the format 'name@domain.com'.")
            continue

        emp_address = input("Enter Employee Address (optional): ")
        if not is_valid_address(emp_address):
            print("Invalid Address. Must contain only alphanumeric characters and spaces.")
            continue
        
        
        return {
            "employee_id": int(emp_id),
            "name": emp_name,
            "email": emp_email,
            "address": emp_address.strip()  
        }

# Main program execution 
#While loops
if __name__ == "__main__":
    employee_records = []
    
    while True:
        employee_info = get_employee_info()
        employee_records.append(employee_info)

        another = input("Would you like to enter another employee? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    print("\nEmployee Records:")
    for record in employee_records:
        if record['address']:
            address_message = "Your address is " + record['address'] + "."
        else:
            address_message = "You did not provide an address."
        
        print("Hello, " + record['name'] + ". Your Employee ID is " + str(record['employee_id']) +
              ", and your email address is " + record['email'] + ". " + address_message)