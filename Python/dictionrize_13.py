# used to key value pair 

# dict = {
#     1:"anil",
#     2:"Sachin",
#     3:"Dipesh",
#     4:"satappa"
# }

# print(dict[3])

phone = {
    "1" :"one",
    "2":"two",
    "3":"three",
    "4":"four",
}

user = input("Phone: ")

for num in user:
    print(phone.get(num,"!"))
