def linearoperation(name, students):
    for student in range(len(students)):
        if(name==students[student]):
            print("Student studies in this class.")
            
students = []
countofnames = int(input("Enter the number of names you want to enter: ")) 
for i in range(1,countofnames+1):
    y = input()
    students.append(y)
name = input("Enter the name you want to search: ")


linearoperation(name, students)