print("----- Student Report -----")
name=input("Student Name: ")
mr1=int(input("Enter subject1 marks: "))
mr2=int(input("Enter subject2 marks: "))
mr3=int(input("Enter subject3 marks: "))
mr4=int(input("Enter subject4 marks: "))
mr5=int(input("Enter subject5 marks: "))
total=500
total_mr=mr1+mr2+mr3+mr4+mr5
percent=(total_mr/total)*100

print("Total mark: ",total_mr)
print(f"Percentage: {percent:.2f}%" )

if percent>=90:
    print("Grade: A")

elif percent >=80 and percent <=89:
    print("Grade: B")

elif percent >=70 and percent <=79:
    print("Grade: C")

elif percent >=60 and percent <=69:
    print("Grade: D")

else:
    print("Grade: F")

if percent >=40:
    print("Result: PASS")

else:
    print("Result: FAIL")


