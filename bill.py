units=int(input("please enter Number of Units you Consumed:"))

if units< 50:
    amount = units * 2.60
    surcharge = 25
elif units <100:
    amount=130 + ((units-50)*3.25)
elif units <200:
    amount=130 + 162.50 +((units-100)*5.26)
else:
    amount=130 +162.50 +((units-200)*8.45)
    surcharge = 75
total = amount +surcharge
print("Electricity Bill:Rs.%.2f"%total)          

