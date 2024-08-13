actual_num= 9

stop = 1


while stop<=3:
    guess = int(input("Guess : "))
    if actual_num==guess:
        print("You won !!! ")
        stop=stop+1
        break
    stop=stop+1

else:
    print("You are failed !!! ")

# use break statement to terminate the loop