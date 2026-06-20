# calculator :
 

operation = input("What math operatoin u need to perform : ('+' , '-' , '*' , '/') : ")

num1 = float(input("Enter a number : "))
num2 = float(input("Enter a Number : "))

if operation == "+":
    result = num1 + num2
    print(result)

elif operation == "-":
    result = num1 - num2
    print(result)

elif operation == "*":
    result = num1*num2
    print(result)

else:
    result = num1/num2
    print(result)

