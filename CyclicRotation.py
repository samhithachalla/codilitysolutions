def solution(A,K):
    if K<len(A):
        output = A[-K:]
        temp=A[:-K]
        output.extend(temp)
    elif len(A)==0:
        output=[]
    elif K==len(A):
        output = A
    elif K>len(A):
        k=K%len(A)
        output = A[-k:]
        temp=A[:-k]
        output.extend(temp)
    return(output
