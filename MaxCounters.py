# Time Complexity O(N*M) expected O(N+M)
def solution(N, A):
    counter=[0]*N
    for i in A:
        if i<=N and i>=1:
            counter[i-1] = counter[i-1]+1
        elif i == (N+1):
            counter=[max(counter)]*N
        else:
            continue
    return(counter)
# Time complexity is O(N*M) -- 40% correctness 100%
def solution(N, A):
    output=[0]*N
    for i in A:
        if i==N+1:
            output=[max(output)]*N
        else:
            output[i-1]=output[i-1]+1
    return(output)
##
