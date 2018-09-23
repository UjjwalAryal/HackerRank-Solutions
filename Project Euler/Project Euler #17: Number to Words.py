digits = {  0:'', 1:'One ', 2:'Two ', 3:'Three ', 4:'Four ', 5:'Five ', 6:'Six ', 7:'Seven ', 8:'Eight ' , 9:'Nine ' , 10:'Ten ' ,\
            11: 'Eleven ', 12: 'Twelve ' , 13: 'Thirteen ' , 14: 'Fourteen ' , 15: 'Fifteen ' , 16: 'Sixteen ' , 17:'Seventeen ',\
            18: 'Eighteen ' , 19: 'Nineteen ' , 20: 'Twenty ' , 30 : 'Thirty ' , 40:'Forty ' , 50: 'Fifty ' , 60:'Sixty ' , \
            70:'Seventy ' , 80:'Eighty ' , 90:'Ninety '
         }

def to_str(n,str_):
    if n >= 100:
        if n%100 >= 20:
            return digits[n//100]+ 'Hundred ' + digits[((n//10)%10)*10] + digits[n%10]  +str_
        else:
            return digits[n//100]+ 'Hundred ' + digits[n%100] + str_
    elif n>=1:
        if n%100 > 20:
            return digits[((n//10)%10)*10] + digits[n%10]  +str_
        else:
            return digits[n%100] + str_
    else:
        return ''
def toWords(n):
    bill , mill , thousand , hundred = (n//10**9), (n//10**6)%(10**3), (n//10**3)%(10**3), n%(10**3)
    return to_str(bill, 'Billion ') + to_str(mill , 'Million ')+ to_str(thousand, 'Thousand ') + to_str(hundred,'')

for _ in range(input()):
    n = input()
    print toWords(n)
