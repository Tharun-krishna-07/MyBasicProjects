# BMI Calculator :
 

weight = float(input("Enter your weight (pounds) : "))

height = float(input ("Enter your height (inches)  : "))



print(f"Your weight is {weight} pounds")
print (f"Your height is {height} ")

bmi = weight / (height **2) * 703

print ("The body mass index (BMI) is ",bmi)

if bmi <= 18.5 :
    print("UnderWeight")
    print("Your health is at minimum make sure u meet the required weight !!!")
elif bmi <= 24.9:
    print("Normal Weight")
elif bmi <= 34.9 :
    print("You are overweight")
elif bmi <=39.9 :
    print("You are obese")
elif bmi >=40 :
    print("You are Morbidly Obese")