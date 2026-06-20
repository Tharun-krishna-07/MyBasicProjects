#Temperature convertor : 

userchoice = input("choose the type of measure u need to convert (Celcius °C) or (fahrenheit °f) : ").casefold()

uservalue = int(input("Enter the value : "))

def celcius_to_fahrenhite():
   f = uservalue * 9/5 + 32

   print(f"{uservalue}°C = {f}°F")



def fahrenhite_to_celcius():
   c = (uservalue - 32) * 5/9
   print(f"{uservalue}°F = {c}°C")



if userchoice == "celcius":
   celcius_to_fahrenhite()
elif userchoice == "fahrenheit" :
   fahrenhite_to_celcius()
else:
   print("Invalid Choice")


