# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
# time efficiency 0 correctness 40%
def solution(A):
    op=[]
    min_val=[]
    if len(A)>0:
        for i in range(0,len(A)-2,1):
            for j in range(2,len(A)-i,1):
                avg_val=float(sum(A[i:i+j]))/len(A[i:i+j])
                if i==0:
                    min_avg=avg_val
                    min_val.extend([min_avg])
                    op.extend([i])
                else:
                    min_avg=min(min_avg,avg_val)
                    if min_avg==avg_val:
                        min_val.extend([min_avg])
                        op.extend([i])
                    else:
                        op=op
        if len(op)==0:
            return(0)
        else:
            return(op[min_val.index(min(min_val))])
    else:
        return(0)
# score 50%
# time efficiency 60%
# correctness 40%

def solution(A):
    op=[]
    min_val=[]
    if len(A)>0:
        for i in range(0,len(A)-2,1):
            avg_val=float(sum(A[i:i+2]))/len(A[i:i+2])
            if i==0:
                min_avg=avg_val
                min_val.extend([min_avg])
                op.extend([i])
            else:
                min_avg=min(min_avg,avg_val)
                if min_avg==avg_val:
                    min_val.extend([min_avg])
                    op.extend([i])
                else:
                    op=op
        if len(op)==0:
            return(0)
        else:
            return(op[min_val.index(min(min_val))])
    else:
        return(0)
## score 100%
#time efficiency 100%
# correctness 100%
def solution(A):
    op=[]
    min_val=[]
    if len(A)>0:
        for i in range(0,len(A)-1,1):
            for j in [2,3]:
                avg_val=float(sum(A[i:i+j]))/len(A[i:i+j])
                if i==0:
                    min_avg=avg_val
                    min_val.extend([min_avg])
                    op.extend([i])
                else:
                    min_avg=min(min_avg,avg_val)
                    if min_avg==avg_val:
                        min_val.extend([min_avg])
                        op.extend([i])
                    else:
                        op=op
        if len(op)==0:
            return(0)
        else:
            return(op[min_val.index(min(min_val))])
    else:
        return(0)
