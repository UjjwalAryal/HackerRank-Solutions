import math
phi = 1.6180339887498948
for _ in range(input()):
    n = input()
    print int(math.ceil((math.log(10) * (n - 1) + math.log(5) / 2) / math.log(phi)))
