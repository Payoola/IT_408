employee_numbers = [1121, 1122, 1127, 1132, 1137, 1138, 1152, 1157]
employee_names = [
    "Jackie Grainger", "Jignesh Thrakkar", "Dion Green", 
    "Jacob Gerber", "Sarah Sanderson", "Brandon Heck", 
    "David Toma", "Charles King"]

employee_salaries = [22.22, 25.25, 28.75, 24.32, 23.45, 25.84, 22.65, 23.75]
total_hourly_rate = [28.886, 32.825, 37.375, 31.616, 30.485, 33.582, 29.445, 30.875]
company_raises = [23.32, 26.31, 29.61, 25.14, 24.18, 26.40, 23.10, 24.20]

#empty list for list of employee record
employee_records = []

#creating data into a list of dictionary items
for i in range(len(employee_numbers)):
    employee_record = {"employee_number": employee_numbers[i],
        "name": employee_names[i],
        "salary": employee_salaries[i],
        "total_hourly_rate": total_hourly_rate[i],
        "new_hourly_rate": company_raises[i]}
    
    employee_records.append(employee_record)

#print final list of employee records
print("employee records:")
for record in employee_records:
    print(record)