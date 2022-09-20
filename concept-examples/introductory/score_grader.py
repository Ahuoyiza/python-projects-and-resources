print("Welcome to the score grader")

name = input("Please input the student name: ")

subject = input("Please input the subject: ")

score = input("Please input student's score: ")

score = int(score)
if score in range(70,100):
    print(name, "got an A" " in", subject )

elif score in range(60,69):
    print(name, "got a B", " in", subject)

elif  score in range(50,59):
     print(name, "got a C", " in", subject)

elif  score in range(40,45):
     print(name, "got a D", " in", subject)

elif  score in range(40,45):
     print(name, "got an E", " in", subject)

elif  score in range(0,39):
     print(name, "got an F", " in", subject)



