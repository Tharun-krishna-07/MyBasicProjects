# grade calculator


name = input("Enter your name : ")

sub = input("Enter the subjects name to check  the grade : ")

mark = float(input(f"Enter the percentage u scored in {sub} "))
print("Name : ",      name)
print("Subject : ",    sub)
print("You scored : ",mark)

#grade segeration :  100 - 90 => A , 89 - 70 => B , 69 - 50 => C , 49 - 35 => D , 34 - 0 => F


if mark >= 90 :
    print("Your Grade : A ") 
elif mark>=70 :
    print("Your grade : B")
elif mark>=50:
    print("Your Grade : C")
elif mark>=35:
    print("Your Grade : D")
else:
    print("Your Grade : F")
    print("You failed the exam.")