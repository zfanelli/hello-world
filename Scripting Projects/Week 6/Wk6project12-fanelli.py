import os

fileName = input("Enter the filename: ")

if not os.path.exists(fileName):
    print("File not found.")
else:
    with open(fileName, 'r') as file:
        print("Payroll Report")
        print("{:<15} {:<15} {:<15}".format("Employee", "Hours Worked", "Wages Paid"))
        print("-" * 45)

        for line in file:
            details, programCode = line.strip().split(" ")
            lastName, hourlyWage, hoursWorked = details.split(",")

            wagesPaid = float(hourlyWage[1:]) * float(hoursWorked[:-1])

            print("{:<15} {:<15} ${:<15.2f}".format(lastName[1:-1], hoursWorked[1:-1], wagesPaid))
