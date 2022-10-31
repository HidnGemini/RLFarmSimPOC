my_list = [10,2,16,827,45]
def findNum(my_list, num):
    for i in range(len(my_list)):
        if my_list[i] == num:
            return i
print(findNum(my_list, 16))