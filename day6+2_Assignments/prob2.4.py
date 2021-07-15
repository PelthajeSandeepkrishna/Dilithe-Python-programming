# Write a program to calculate the grade. The grade should be calculated in the following method.

score = int(input("Enter Score : "))

if score in range(1,101):
    if score >= 90:
        print("Grade O")
    elif score >= 80:
        print("Grade A+")
    elif score >= 70:
        print("Grade A")
    elif score >= 60:
        print("Grade B+")
    elif score >= 50:
        print("Grade B")
    else:
        print("No Grade")
