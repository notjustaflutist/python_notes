employee_file = open("employees.txt", "a") # "w" will overwrite or create a new file
#  employee_file.write("Toby - Human Resources")
#  print(employee_file.read())

employee_file.write("\nKelly - Customer Service")
employee_file.close()
