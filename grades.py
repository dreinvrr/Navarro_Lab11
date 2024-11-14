grades = []
passed_students = []
valid_input = True

print("\nHello there! Please enter student grades between 40 to 100.")
print("If you typed below 39, the system won't accept it.\n")
while True: #Entering the grade
    grade = input("Please enter your grade (Type 'done' if you're finish): ")
    
    if grade.lower() == 'done':
        print("\nSuccess!\n")
        break #Para tumigil yung pag lagay ng grade
    if not grade.isdigit(): 
        print("Invalid input. Please enter a number.")
    else:
        grade = int(grade)
        if grade <= 40 or grade > 100:
            print("Invalid data, Please try again.")
            valid_input = False
            break
        else:
            grades.append(grade)
            if grade >= 75:
                passed_students.append(grade)
                
if valid_input:    
    if grades:
        
        average_grade = sum(grades) / len(grades)
        passing_percentage = (len(passed_students) / len(grades)) * 100
        print(f"Average Grade is: {average_grade:.2f}")
        print(f"The Passing Percentage is: {passing_percentage:.2f}%\n")
        print(f"The number of students who passed: {len(passed_students)}")
        print(f"Grades: {passed_students}\n")
    else:
        print("No grades were entered")
        
        
        
        