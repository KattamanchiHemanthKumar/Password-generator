def dup(l):
    l1=[]
    l2=[]
    # for i in l:
    #     if i not in l1:
    #         l1.append(i)
    # print(l1)
    #     # else:
        #     l2.append(i)
        #     print(l2)
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]==l[j] and l[i] not in l1:
                l1.append(l[i])
    print(l1)
    
l=input().split()
l=list(map(int,l))
dup(l)