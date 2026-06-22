numbers = []

n = int(input("Enter how many numbers you need to check :" ))

for i in range (n) :
    num = int(input(f"Enter the number {i+1}:"))
    numbers.append(num)

for num in numbers :
    if num>0 :
        print(f"{num} is positive")
    elif num<0 :
        print(f"{num} is negative")
    else:
        print(f"{num} its zero")
