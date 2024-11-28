data = [1121, "Jackie Grainger", 22.22,
 1122, "Jignesh Thrakkar", 25.25,
 1127, "Dion Green", 28.75, False,
 24.32, 1132, "Jacob Gerber",
 "Sarah Sanderson", 23.45, 1137, True,
 "Brandon Heck", 1138, 25.84, True,
 1152, "David Toma", 22.65,
 23.75, 1157, "Charles King", False,
 "Jackie Grainger", 1121, 22.22, False,
 22.65, 1152, "David Toma"]


employee_numbers = []
employee_names = []
employee_salaries = []

temp_salary = None

for item in data:
    if isinstance(item, int):
        employee_numbers.append(item)
    elif isinstance(item, str):
        employee_names.append(item)
    elif isinstance(item, float):
        employee_salaries.append(item)

print("Employee Numbers:", employee_numbers)
print("Employee Names:", employee_names)
print("Employee Salaries:", employee_salaries)

employee_salaries = [
    22.22, 25.25, 28.75, 24.32, 
    23.45, 25.84, 22.65, 23.75,
    22.22, 22.65]

total_hourly_rate = []

for salary in employee_salaries:
    total = salary * 1.3
    total_hourly_rate.append(total)

max_hourly_rate = max(total_hourly_rate)

if max_hourly_rate > 37.30:
    print("Warning: Someone's salary may be a budget concern.")

print("Total Hourly Rates:", total_hourly_rate)
print("Maximum Total Hourly Rate:", max_hourly_rate)

underpaid_salaries = []

for salary in employee_salaries:
    total = salary * 1.3
    total_hourly_rate.append(total)

    if 28.15 <= total <= 30.65:
        underpaid_salaries.append(total)

max_hourly_rate = max(total_hourly_rate)

print("Underpaid Salaries:", underpaid_salaries)

company_raises = []
 
for salary in employee_salaries:
    if 22 <= salary < 24:
        raise_amount = salary * 0.05
    elif 24 <= salary < 26:
        raise_amount = salary * 0.04
    elif 26 <= salary < 28:
        raise_amount = salary * 0.03
    else:
        raise_amount = salary * 0.02 
    
    new_salary = salary + raise_amount
    company_raises.append(new_salary)

print("Original Salaries:", employee_salaries)
print("Salaries after Raises:", company_raises)

for salary in employee_salaries:
    if salary > 22:
        if salary < 30:
            if salary != 25.84:
                if round(salary * 100) % 2 == 0:
                    print(f"the salary {salary} meets all the conditions")
                else:
                    print(f"the salary {salary} is not even when considering two decimal places")
            else:
                print(f"the salary {salary} is equal to 25.84, which is excluded.")
        else:
            print(f"the salary {salary} is not less than $30.")
    else:
        print(f"the salary {salary} is not greater than $22.")
#the statement checks:
    #if the salary is greater than $22
    #if the salary is less than $30
    #if the salary is not equal to $25.84
    #if the salary is even when multiplied by 100
#if all conditions are met, it will print that the salary meets the conditions.
#if not, it provides feedback on which specific conditions was not met


