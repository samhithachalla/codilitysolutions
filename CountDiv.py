#CountDiv -- 100%
def solution(A, B, K):
    if A!=B:
        if A%K == 0:
            return(int(B/K)-int(A/K)+1)
        else:
            return(int(B/K)-int(A/K))
    else:
        if A%K == 0:
            return(1)
        else:
            return(0)
