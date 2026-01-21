import random
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
dict = {"s" : 1,"w" : -1,"g" : 0}
reverseDict = {1 : "Snake",-1 : "Water",0 : "Gun"}
you = dict[youstr]

#According to program Now we have 2 number first is "computer". Second is "you"
print(f"You chose {reverseDict[you]}\nand computer choose {reverseDict[computer]}")

if(computer ==you):
    print("draw")
else:
    if((computer - you) == -1 or (computer - you) == 2):
        print("you lose!")

    else:
        print("you win!")

# Short code with pattern observation