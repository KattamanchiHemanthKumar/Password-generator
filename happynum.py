'''n=int(input("len"))
l=[]
for i in range(n):
    val=input("ele")
    l.append(val)
print(l)

'''
"""
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""

n=int(input("enter num"))#19
temp=n
def ishappy(n):
    r=0
    while n>0:
        t=n%10
        r=r+t*t
        n=n//10
    return r
while temp!=1 and temp!=4:
    temp=ishappy(temp)
if temp==1:
    print("happy")
elif temp==4:
    print("not happy")
