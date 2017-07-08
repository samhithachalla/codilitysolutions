##genome impace factor
#time 33%
##correctness 100
#total -75%
def solution(S, P, Q):
    op=[]
    for i in zip(P,Q):
        gen = S[i[0]:(i[1]+1)]
        if 'A' in gen:
            op.extend([1])
        elif 'C' in gen:
            op.extend([2])
        elif 'G' in gen:
            op.extend([3])
        else:
            op.extend([4])
    return(op)

#silly me i forgot the set idea
