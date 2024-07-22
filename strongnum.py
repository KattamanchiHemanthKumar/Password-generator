# n=int(input())
# t=n
# s=0
# while n>0:
#     i=1
#     f=1
#     rem=n%10
#     while i<=rem:
#         f*=i
#         i+=1
#     s+=f
#     n=n//10
# if s==t:
#     print("strong num")
# else:
#     print("not strong")
"""
1! + 4! + 5!
1 + 24 + 120
145
"""
def strong(n):
    t=n
    s=0
    while n>0:
        i=1
        f=1
        rem=n%10
        while i<=rem:
            f*=i
            i+=1
        s+=f
        n=n//10
    if s==t:
        print("s")
    else:
        print("ns")
n=int(input())#145
strong(n)