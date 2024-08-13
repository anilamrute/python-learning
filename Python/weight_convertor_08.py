from math import floor


weigth = float(input("Weight : "))

parameter = input("(L)bs OR (K)g : ")

parameter.lower()

if parameter == "l":
    corrected_weight = weigth*2.02
    print(f"You are {corrected_weight} Lbs")
else:
    corrected_weight = weigth/2.02
    print(f"You are  {round(corrected_weight)} kg")