def makeStateTable(P):
    """construct the pie table"""

    m = len(P)
    pieTb = {i:0 for i in range(1,m+1)}
    pieTb[0] = 0
    pieTb[1] = 0
    i = 0 # longest presuffix has been found
    j = 2
    while j <= m:

        while i>0 and P[i] != P[j-1]:
            i = pieTb[i]
        if P[i] == P[j-1]:
            i = i + 1
        pieTb[j] = i

        j = j +1
    return pieTb



def search(text,strPtn):
    """search string pattern strPtn in text,
    return position matched"""


    # construct pie Table that holds the number of characters
    # matched if fail at the current step

    pieTb = makeStateTable(strPtn)

    position = [] #position matched
    i = 0 # position to be matched in text
    q = -1 # number of characters matched so far

    while (i < len(text)):

        print('i=%i,q=%i'%(i,q))
        if text[i] == strPtn[q+1]:
            # mached one character
            q = q + 1

            if q == len(strPtn) - 1:
                q = pieTb[q]
                print('matched at %i'%i)
                position.append(i-len(strPtn)+1)
            i = i + 1
        else:
            # if not matched, try go back one step
            q = pieTb[q]

            # if back to epsilon, start from beginning
            if q == 0:
                i = i + 1
    return position
