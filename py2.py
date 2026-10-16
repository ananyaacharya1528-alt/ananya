principal=int(input("Enter the amount:"))
rate=int(input("Enter rate:"))
time=int(input("Enter time in years:"))

Intrest=principal*rate*time/100
total_amount=principal+Intrest

print("Simple Intrest=",Intrest)
print("Total Amount=",total_amount)
      