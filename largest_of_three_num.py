# to find the largest of three number :

num1 = float(input("Enter a number : "))
num2 = float(input("Enter a number : "))
num3 = float(input("Enter a number : "))

if (num1 >=num2) and (num1>=num3):
    print(f"The greatest number between {num1} , {num2} , {num3} is {num1} ")
elif (num2 >= num1) and (num2 >= num3):
    print(f"The greatest number between {num1} , {num2} , {num3} is {num2} ")
else:
    print(f"The greatest number between {num1} , {num2} , {num3} is {num3} ")