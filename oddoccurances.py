def solution(A):
    A=sorted(A)
    output=None
    if len(A)==1:
        return(A[0])
    else:
        for i in range(len(A)-1):
            if i%2==0:
                if A[i]^A[i+1]!=0:
                    output=A[i]
                    return(output)
                    break
                else:
                    continue
        if output==None:
            return(A[-1])
