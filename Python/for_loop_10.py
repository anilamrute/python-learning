#Itertrate over items in collection

# for item in "Python":
#     print(item)


# for item in [1,2,3,4,5,6,11]:
#     print(item)

# for item in range(1,11 , 3 ):  # range() , create a object to range  , take start , end and also we define step 
#     print(item)

# for item in ["Ansh", "Ashu" , "Bhairav"]:
#     print(item)


prices = [10,20,30,40]
sum = 0
for price in prices:
    sum = sum + price
print( f"price of the list: {sum}")