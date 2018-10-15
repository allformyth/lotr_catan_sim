import random

for i in range(100):
    result = 0
    for j in range(2):
        tmp = random.randint(1, 6)
        print(tmp)
        result = result + tmp
    print(result)
    print("-----------------")