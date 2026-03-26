subjects = []
difficulty = []
days_left = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    sub = input("Enter subject name: ")
    diff = int(input("Enter difficulty (1=Easy, 2=Medium, 3=Hard): "))
    days = int(input("Days left for exam: "))
    
    subjects.append(sub)
    difficulty.append(diff)
    days_left.append(days)

priority = []

for i in range(n):
    score = difficulty[i] / days_left[i]
    priority.append(score)

combined = list(zip(subjects, priority))
combined.sort(key=lambda x: x[1], reverse=True)

print("\nYour Smart Study Plan:\n")

day = 1

for sub, score in combined:
    print("Day", day, "-> Study", sub)
    day += 1
