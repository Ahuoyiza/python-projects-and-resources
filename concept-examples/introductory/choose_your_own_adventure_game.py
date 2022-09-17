name = input("Welcome brave one, What is your name: ")
print("welcome", name, "to this adventure")

answer = input(
    "you ahve come to the end of the road and you can go left or right. which way would you like to go: ").lower()
if answer == "left":
    q2 = input("you come to a river, you walk around it or swim across ? Type walk to walk around and swim to swim across ")

    if q2 == "swim".lower():
        print("you swam across and were eaten by an alligator.")

    elif q2 == "walk":
        print("you walked till you ran out of water and you lost the game")
    else:
         print("not a valid option good bye") 

elif answer == "right":
    answer = input("you come to a bridge, it's wobbly, do you want to cross it or head back (cross/back) ? ")
     
    if answer == "back".lower():
        print("you go back and lose")

    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger. Do you talk to them (yes/no)?  ")
        
        if answer == "yes":
            print("you talk to the stranger and they give you gold.You WIN")

        elif answer == "no":
            print("you ignore the stranger and the are offended and you lose")

    else:
         print("not a valid option good bye") 
else:
    print("not a valid option good bye")

print("Thank You for trying", name)