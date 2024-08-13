# names = ['Anil', 'Rahul', 'sachin','dipesh', 'kalu']

# print(names[4])

# numbers = [10,30,17,5,7,40,67,92]

# large_num = 0
# for num in numbers:
#     if num >large_num:
#         large_num = num 
# print(large_num)

# 2D list / list in list

# matrix = [
#     [1,2,3],
#     [4,5,6], 
#     [7,8,9]
# ]

# print(matrix[1][2])

# for row in matrix:
#     for item in row:
#         print(item)

# -----------------------------------------

# List Method 

# numbers = [2,4,5,7,9,5,10,30]
# numbers.append(30)# add new item , will add in the end 

# print(numbers)  
# numbers.insert(2,30)# add new item , we can wherever
# numbers.remove(30) # remove mentioned num 
# numbers.clear() # clear all content
# print(numbers.index(5)) # return index of the num ,if not exit return error

# print(50 in numbers) # retrun boolean not error 

# print(numbers.count(5)) # return hou many times num is prsent in list
# # print(numbers)  # add new item , we can  add with index  

# numbers.sort() # sort in ascending order
# numbers.reverse() # will desc

# num2 = numbers.copy() # if we do modify then not wil update on original list
# print(num2)


numbers = [1,3,4,5,1,7,8,9, 6 ,7,6 ,7]
print(numbers)
uniq = []
for num in numbers:
    if num not in uniq:
        uniq.append(num)
print(uniq)

