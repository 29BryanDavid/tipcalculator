bill = float(input("Enter the total bill amount"))
tip = int(input("Enter how much percnet tip you want to give?"))
people = int(input("Enter the number of people you per person tip included!"))
totbillamt = tip / 100 * bill + bill
print("Now total bill with considering the tip is", int(totbillamt))
billperperson = totbillamt / people
print("Each person should pay", round(billperperson))
