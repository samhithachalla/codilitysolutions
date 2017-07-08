def solution(A):
    lst=[]
    for i in range(1,len(A),1):
        diff_sum = abs(sum(A) - (2*sum(A[:i])))
        lst.extend([diff_sum])
    return(min(lst))

## to get a 100% in time complexity



