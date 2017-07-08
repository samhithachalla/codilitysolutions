
def solution(S):
    round_1=[]
    square=[]
    curly=[]
    a=0
    if len(S)==0:
        return(1)
    elif len(S)%2 ==1:
        return(0)
    else:
        if S.count('[')==S.count(']') and S.count('{')==S.count('}') and S.count('(')==S.count(')'):
            # create index of all ending points
            for i in range(len(S)):
                round_1.extend([S.find(')',i)])
                square.extend([S.find(']',i)])
                curly.extend([S.find('}',i)])
            # if index of all starting points is away by 0 or even numbers op 1
            for i in range(len(round_1)):
                if S[a:round_1[i]].find('(')
                a=i
        else:
            return(0)
##########
def solution(S):
    round_1=[]
    square=[]
    curly=[]
    a=0
    if len(S)==0:
        return(1)
    elif len(S)%2 ==1:
        return(0)
    else:
        if S.count('[')==S.count(']') and S.count('{')==S.count('}') and S.count('(')==S.count(')'):
            # create index of all ending points
            for i in range(len(S)):
                round_1.extend([S.find(')',i)])
                square.extend([S.find(']',i)])
                curly.extend([S.find('}',i)])
            # if index of all starting points is away by 0 or even numbers op 1
            for i in range(len(round_1)):
                if S[a:round_1[i]].find('(')
                a=i
        else:
            return(0)
