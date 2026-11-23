# Student Grade Calculator
print("=====================")
print("Student Grade Calculator")
print("=====================") 

name = input("Enter the student's name: ")

mark1 = float(input("Enter subject 1 mark: "))
mark2 = float(input("Enter subject 2 mark: "))
mark3 = float(input("Enter subject 3 mark: "))

total = mark1 + mark2 + mark3
average = total / 3

if average >= 75:
    grade = "A"
elif average >= 65:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 35:
   grade = "S"
else:
    grade = "F"

print("\n===== Student Result =====")  
print("Name : ", name)
print("Total Marks : ", total)
print("Average Marks : ", average)  
print("Grade : ", grade)
print("===========================")   