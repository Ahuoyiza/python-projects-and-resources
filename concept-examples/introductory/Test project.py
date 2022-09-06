print("Welcome To the my first test Quiz!!")

playing = input("Do you want to play my game? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's play:) ")
score = 0

answer = input("What are we learning today? ")
if answer.lower() == "python":
    print("That's correct good job :)")
    score += 1
else:
    print("incorrect please try again :( ")

answer = input("What shape is a pizza ? ")
if answer.lower() == "round":
    print("That's correct good job :)")
    score += 1
else:
    print("incorrect please try again :( ")

answer = input("What is the meaning of USB? ")
if answer.lower() == "universal serial bus":
    print("That's correct good job :)")
    score += 1
else:
    print("incorrect please try again :( ")

answer = input("What is the first day of the week? ")
if answer.lower() == "sunday":
    print("That's correct good job :)")
    score += 1
else:
    print("incorrect please try again :( ")

print("you got " + str(score) + " questions correct!")
