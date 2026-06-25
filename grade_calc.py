grade = []
subjects = []

count = int(input("Enter how many subject marks you need to check : "))

for i in range(count):
    sub= input(f"Enter the subject{i+1} : ")
    subjects.append(sub)

for sub in subjects:
    score = int(input(f"Enter your scores in {sub} :"))
    grade.append(score)

for sub, score in zip(subjects, grade):
    if score >= 90:
        print(f"{sub}: {score}% → Grade A")
    elif score >= 80:
        print(f"{sub}: {score}% → Grade B")
    elif score >= 70:
        print(f"{sub}: {score}% → Grade C")
    elif score >= 60:
        print(f"{sub}: {score}% → Grade D")
    else:
        print(f"{sub}: {score}% → Grade F")