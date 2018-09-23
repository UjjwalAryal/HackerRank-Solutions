import sys
print '\n'.join(map(str,[((4 * n**3 + 3*n**2 + 8*n - 15)/6 + 1) % (10**9 + 7) for n in map(int,sys.stdin.read().strip().split('\n')[1:])]))

# Alternate Solution
#
# for _ in range(input()):
#     n = input()
#     print (4*(((n*(n+1)*(n+2))/6)-1)- 6 * ((n**2 - 1)/4) + 1) % (10**9 + 7)
