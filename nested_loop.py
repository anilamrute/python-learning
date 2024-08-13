# if loops in loop called nested loops


# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')


number = [5,2,5,2,2]

for num in number:
        output=''
        for i in range(num):
            output += "*"
        print(output)
