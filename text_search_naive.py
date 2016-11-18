

qtb={0:'',1:'a',2:'b',3:'a',4:'b',5:'a',6:'c',7:'a'}
pitb={0:0,1:0,2:0,3:1,4:2,5:3,6:0,7:1}

state = 0

def matchChar(char):
    """match single character"""

    global state

    print('state=%i'%state)
    if char == qtb[state+1]:
        state = state + 1
        print('matched %s'%char)
        if state == 7:
            state = pitb[state]
            print('matched pattern')
        return
    else:
        if state == 0:
            return
        state = pitb[state]
        matchChar(char)

strPtn = 'ababaca'
textstr = 'ababacababca'

def matchString(textstr,strPtn):
    "match string pattern in a string"
    for char in textstr:
        matchChar(char)

# max suffix preffix
def maxSufPrefix(mystr):

    for i in range(1,len(mystr)):
        if mystr[i:] == mystr[:-i]:
            return mystr[i:]
    return ''

# construct the state table

def makeStateTable(strPtn):
    """construct the state table from string pattern"""

    qTb = {i+1:strPtn[i] for i in range(len(strPtn))}
    qTb[0] = ''
    pTb = {}

    matchedStr = ''
    for i in range(0,len(strPtn)+1):
        matchedStr = matchedStr + qTb[i]
        pTb[i] = len(maxSufPrefix(matchedStr))
    return qTb,pTb

# put together

def searchString(textStr,strPtn):
    """string search, return the positions that the pattern are founded"""

    global state 
    global matched
    global matchedPos

    state = 0
    matched = 0
    matchedPos = []

    qTb,pTb = makeStateTable(strPtn)


    def matchChar(char):
        """match single character"""

        global state, matched, matchedPos

        print('state=%i'%state)
        if char == qTb[state+1]:
            state = state + 1
            print('matched %s'%char)
            if state == len(strPtn):
                state = pTb[state]
                matched = 1
            return
        else:
            if state == 0:
                return
            state = pTb[state]
            matchChar(char)

    i = 0
    for char in textstr:
        matched = 0
        matchChar(char)
        if matched == 1:
            matchedPos.append(i-len(strPtn)+1)
        i = i+1

    return matchedPos

