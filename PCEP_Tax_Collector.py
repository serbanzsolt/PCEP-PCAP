income = float(input("Enter the annual income: "))
tax = 0

if income < 85528:
    tax = (income*0.18) - 556
else:
    tax = 14839.02 + ((income-85528))*0.32

tax = round(tax, 0)
if tax <=0:
    print("The tax is: 0.0 thalers")
else:
    print("The tax is:", tax, "thalers")
