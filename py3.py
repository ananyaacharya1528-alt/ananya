name=input("Sudent name:")
USN=input("enter USN:")

marks1=float(input("enter marks in course1:"))
marks2=float(input("enter marks in course2:"))
marks3=float(input("enter marks in course3:"))

print("|n student details")
print("Name:",name)
print("USN:",name)
print("cousre 1 marks:",marks1)
print("course 2 marks:",marks2)
print("course 3 marks:",marks3)

total=marks1+marks2+marks3
average=total/3

print("total marks:",total)
print(f" average={average:.2f}")