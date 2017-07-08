##Time Complexity O(N**2) -- 54%

def solution(X, A):
    if len(A)>=X:
        perfect = list(range(1,X+1,1))
        for i in xrange(X,len(A)+1,1):
            set_comp = list(set(A[:i]))
            if perfect == set_comp:
                return(i-1)
                break
            else:
                if i==len(A):
                    return(-1)
                else:
                    continue
    else:
        return(-1)
#########################################################
##Better/same performance with small code - 63%
def solution(X, A):
    lst=[]
    for i in range(1,X+1,1):
        try:
            lst.extend([A.index(i)])
        except ValueError:
            return(-1)
    return(max(lst))
#########################################################
##searching for better performance - 63%
def solution(X, A):
    max_op = 0
    for i in range(1,X+1,1):
        try:
            current = A.index(i)
            max_op = max(current,max_op)
        except ValueError:
            return(-1)
    return(max_op)
###########################################################
## best solution 100%

def solution(X, A):
    m= [1]*X
    if len(set(A))==X:
        for index,element in enumerate(A):
            if m[element-1]==1:
                m[element-1]=0
                X=X-1
                if X==0:
                    return(index)
            else:
                continue
    else:
        return(-1)
