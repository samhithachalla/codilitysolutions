##100 correctness
##100 timelyness
def solution(A):
    A=sorted(A)
    if A[0]>=0 or A[-1]<0:
        return(A[-3]*A[-2]*A[-1])
    elif A[-3]>0:
        return(A[-1]*(max(A[0]*A[1],A[-3]*A[-2])))
    elif A[-2]>0 and A[-3]<0:
        return(A[0]*A[1]*A[-1])
    elif A[-1]>0 and A[-2]<0:
        return(A[0]*A[1]*A[-1])
    elif A[-1]==0:
        return(0)
