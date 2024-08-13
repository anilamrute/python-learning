quite = True

start = False

stop = False

while quit:
    help= input(">").lower()

    if help == "help":
        print("start - to start the car ")
        print("stop - to stop the car ")
        print("quite - to exit ")
        
    elif help== "start":
        if start == True:
            print("car is already start ")
        else:
            start = True
            print("car is start ..Ready to Go...")
            stop=False
    elif help== "stop":
        if stop == True:
            print("car is already stop ")
        else:
            stop = True
            print("car is stopped.")
            start=False
    elif help== "quite":
        quit =False
    else:
        print("i dont understand that ...")


