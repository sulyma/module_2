my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
len_ = len(my_list)
index_ = 0
while index_ < len_:
    if my_list[index_] < 0:
        break
    elif my_list[index_] == 0:
        index_ = index_ + 1
        continue
    else:
        print(my_list[index_])
        index_ = index_ + 1