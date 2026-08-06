rent = float(input("enter your rent"))

if rent < 85528:
    tax = rent * 0.18 - 556.02
else:
    tax = (rent - 85528) * 0.32 + 14839.02

if tax < 0.0:
    tax = 0.0 

tax = round(tax, 0)
print("the tax is", tax, "thalers")