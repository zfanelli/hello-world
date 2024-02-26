salary = float(input("Enter the starting salary for teachers: "))

percentage = float(input("Enter the percentage increase for each year: "))
                                  
years = int(input("Enter the number of years in the schedule: "))

print("Year Salary")

salaryNow = salary
for year in range(1, years + 1):
    print(str(year) + " $" + str(salaryNow))
    salaryNow += salaryNow * (percentage / 100)

print("After " + str(years) + " years, the final salary is: $" + str(salaryNow))
