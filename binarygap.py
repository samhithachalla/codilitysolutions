def solution(N):
    lst=[]
    bin = "{0:b}".format(N)
    if bin.count("0")!=0:
        for i in range(len(bin)):
            if bin[i]=="1":
                next = bin.find("1",i+1)
                if next !=-1:
                    lst.extend([next-i-1])
                else:
                    lst.extend([0])
            else:
                m=0
        return(max(lst))
    else:
        return(0)
