employee_file = open("employees.txt", "r")

print(employee_file.readable())
print(employee_file.read())
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readlines()) # puts in an array

for employee in employee_file.readlines():
    print(employee)


employee_file.close()  # closes file
# opens a read-only file which is in the same directory
# "w" write file, "a" append, "r+" read/write
