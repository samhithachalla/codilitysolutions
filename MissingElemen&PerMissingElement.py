# Missing Integer -- 100
def solution(A):
    m=1
    A=sorted(set([a for a in A if a>0]))
    if len(A)>0 and len(A)!=max(A):
        for i in A:
            if i>m:
                return(m)
                break
            else:
                m=m+1
    elif len(A)>0 and len(A)==max(A):
        return(max(A)+1)
    else:
        return(1)
    
