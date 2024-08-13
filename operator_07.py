# # use when we have multiple conditiomn 

# has_high_income=False
# has_good_credit=False


# # AND - both condition are true 
# # OR - if one condition is false  
# # NOT - True 

# if has_high_income or has_good_credit:
#     print("Eligible for loan")
# else:
#     print("Not Eligible for loan")

# Camparision Operator 
# when we have to compare value 

# temperature = 24

# if temperature> 30 :
#     print("Its hot day ")
# elif temperature<10:
#     print("Its cold day ")
# else:
#     print("Its neither cold nor  hot")


name = input("Enter name here : ")

char = len(name)

if char < 3 :
    print("Name must be at least 3 character ")
elif char > 50 :
    print("Name can be maximum of 50 character ")
else:
    print("Name looks good!" + name)