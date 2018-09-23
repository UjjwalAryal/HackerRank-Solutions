palindrome = []
for i in range(100,1000):
    for j in range(100,1000):
        n = str(i*j)
        if n == n[::-1]:
            palindrome.append(int(n))
palindrome.sort()
for _ in range(input()):
    n = input()
    for i in range(len(palindrome)-1,-1,-1):
        if palindrome[i] < n:
            print palindrome[i]
        else:
            continue
        break
    
