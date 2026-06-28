import random
options = ("rock","paper","scissor")
computer = random.choice(options)
p=0
c=0

while True:
    print("1.rock"
          "2.paper"
          "3.scissor")
    x=input("Enter Ur option(Q for quit)")
    if x=="rock" and computer=="paper":
        c+=1
    elif x=="paper" and computer=="scissor":
        c+=1
    elif x=="scissor" and computer=="rock":
        c+=1
    elif x.lower()=="q":
        break
    elif x not in options:
        continue
    else:
        p+=1
    print(f"Computer=={computer},User={x}")
    print(f"score Computer={c},user={p}")
