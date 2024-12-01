salaries_list = list(map(float, input("Enter employee salaries separated by spaces: ").split()))
avg_salary = average_salary(salaries_list)
print("The average salary is:", avg_salary)