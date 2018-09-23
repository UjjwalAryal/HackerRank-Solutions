def grade(a):
    if a<38  or  a%5==0:
        return a
    x= 5-(a%5)
    if x<3:
        return a+x
    return a
for _ in range(input()):
    x=input()
    print grade(x)
