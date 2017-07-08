#Passing Cars -- 50% --O(N**2) no pints in time complexity
def solution(A):
    op=0
    for i in range(len(A)):
        if A[i]==0:
            op=op+A[i:].count(1)
        else:
            continue
    if op<=1000000000:
        return(op)
    else:
        return(-1)
#Passing Cars -- 100% -- time complexity-0
def solution(A):
    op=0
    X = [i for i in range(len(A)) if A[i]==0]
    for i in X:
        op=op+A[i:].count(1)        
    if op<=1000000000:
        return(op)
    else:
        return(-1)
#Passing Cars -- 60% coorrect --time complexity 0
def solution(A):
    we_lst=[i for i in range(len(A)) if A[i]==1]
    ea_lst=[j for j in range(len(A)) if A[j]==0]
    if len(ea_lst)>1 and len(we_lst)>1:
        j=0
        tup_lst=[(x,y) for x in ea_lst for y in we_lst if x < y]
        return(len(tup_lst))
    else:
        return(-1)
#Passing Cars --100 -- time complexity --20
def solution(A):
    op=0
    X = [i for i in range(len(A)) if A[i]==0]
    for i in X:
        op=op+sum(A[i:])        
    if op<=1000000000:
        return(op)
    else:
        return(-1)
