hourlyWage = float(input("Please enter your hourly wage: "))

totalRegular = float(input("Please enter the total regular hours worked: "))

totalOvertime = float(input("Please enter the total overtime hours worked: "))

pay = hourlyWage * totalRegular

overtimePay = totalOvertime * 1.5 * hourlyWage

totalPay = pay + overtimePay

print("Your total pay for this week is $" + str(totalPay))


