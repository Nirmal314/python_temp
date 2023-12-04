n = int(input("Enter the number of employees: "))
employee_dict = {input("Enter employee name: "): float(input("Enter salary: ")) for _ in range(n)}

max_salary_employee = max(employee_dict, key=employee_dict.get)

print("\nDictionary content:")
print(employee_dict)
print(f"\nEmployee with highest salary: {max_salary_employee} - Salary: {employee_dict[max_salary_employee]}")
