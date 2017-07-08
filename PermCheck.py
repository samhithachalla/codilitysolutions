def solution(A):
    sorted_perfect = list(range(1,(len(A)+1)))
    A=sorted(A)
    result = [a-b for (a,b) in zip(sorted_perfect,A)]
    if result.count(0) == len(A):
        return(1)
    else:
        return(0)
