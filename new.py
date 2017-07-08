def solution(A):
    op=[]
    A=sorted(A)
    m=len(A)
    len_i=m-2
    len_j=m-1
    len_k=m
    if len(A)>=3:
        for i in range(len_i):
            for j in range(i+1,len_j,1):
                for k in range(j+1,len_k,1):
                    if (A[i]+A[j]>A[k]) and (A[i]+A[k]>A[j]) and (A[j]+A[k]>A[i]):
                        op.extend([1])
                        break
                    else:
                        op.extend([0])
        return(sum(op))
    else:
        return(0)
