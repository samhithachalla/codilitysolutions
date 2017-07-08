# 100% - correctness
# 12% - time accuracy
def solution(A):
    inst = 0
    for i in range((len(A)-1)):
        for j in range(i+1,len(A),1):
            d=abs(i-j)
            r1=A[i]
            r2=A[j]
            if r1+r2 < d:
                inst = inst
            elif abs(r1-r2)==d:
                inst = inst + 1
            elif r1+r2 == d:
                inst = inst +1
            elif r1+r2 > d:
                inst = inst+1
    return(inst)
 

