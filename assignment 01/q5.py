#Q5. The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
# ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
# Average Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F

sub1=int(input("Enter marks of 1st subject out of 100: "))
sub2=int(input("Enter marks of 2nd subject out of 100: "))
sub3=int(input("Enter marks of 3rd subject out of 100: "))

avg=((sub1+sub2+sub3)/3)

if avg<=100 and avg>=90:
    print(f"congratulations you got A grade")

if avg<=89 and avg>=80:
    print(f"congratulations you got B grade")

if avg<=79 and avg>=70:
    print(f"congratulations you got C grade")

if avg<=69 and avg>=60:
    print(f"congratulations you got D grade")

if avg<=59 and avg>=0:
    print(f"In exam you are failed")

