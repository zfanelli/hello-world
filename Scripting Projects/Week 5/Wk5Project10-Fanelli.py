import math

purchasePrice = float(input("Enter the purchase price: "))

downRate = 0.10
annualRate = 0.12
monthlyRate = annualRate / 12
monthlyRate = 0.05

downPayment = purchasePrice * downRate
balance = purchasePrice - downPayment

print("\nPayment Schedule")
print("Month   Total Balance   Interest   Principal   Payment")

month = 1

numMonths = math.ceil(math.log((monthlyRate * purchasePrice) / (monthlyRate * purchasePrice - balance * monthlyRate), 1 + monthlyRate))

for month in range(1, numMonths + 1):
    interest = balance * monthlyRate
    # Ensure principal does not exceed remaining balance
    if balance <= monthlyRate * purchasePrice:
        principal = balance
    else:
        principal = monthlyRate * purchasePrice - interest
    payment = interest + principal
    balance -= principal
    #Had to look up how to space out the columns because it didn't look good.
    print("{:<7} {:<15.2f} {:<11.2f} {:<11.2f} {:<11.2f}".format(month, balance + downPayment, interest, principal, payment))

print("\nLoan paid off in", numMonths, "months.")

