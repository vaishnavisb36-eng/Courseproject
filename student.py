
name = input("Enter Student Name: ")

marks = []

for i in range(1, 6):
    mark = int(input("Enter Mark " + str(i) + ": "))
    marks.append(mark)

total = sum(marks)
average = total / 5
percentage = (total / 500) * 100

print("\n----- STUDENT REPORT -----")
print("Student Name:", name)
print("Marks:", marks)
print("Total Marks:", total)
print("Average:", average)
print("Percentage:", percentage, "%")

if all(mark >= 35 for mark in marks):
    print("Result: PASS")
else:
    print("Result: FAIL")
