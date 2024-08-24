import random

first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
random_ = random.choice(first_list[2:20])
print(random_)
result = []
for i in first_list[0:len(first_list) - 1]:
    for j in first_list:
        if random_ % (first_list[i - 1] + first_list[j - 1]) == 0 and i < j:
            result.append(first_list[i - 1])
            result.append(first_list[j - 1])

print(*result)
