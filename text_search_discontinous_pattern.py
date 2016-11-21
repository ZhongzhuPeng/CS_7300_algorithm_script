# find the position that matches the shortest sequence consistent with the pattern P
# for example [a,a,c,b,a,c,b,b,a,c] match [a,b,c] returns [1,3,5]
# for example [a,a,c,b,a,c,b,b,a,c] match [a,b,c,a] returns [1,3,5,8]
# this function is equivilant to Mathematica expression:
# First@SortBy[StringPosition["aacbacbbac", "a" ~~ Shortest[__] ~~ "b" ~~ Shortest[__] ~~ "c"],Abs[Differences@#] &]

#xs = "aacbacbbac"
#p = "abca"


def match_shortest_sequence(xs,p):

    dic = {} # record all the positions of the character in the pattern in the text

    matched = [] # possible shortest matched position

    for c in p:
        dic[c] = []

    for (i,c) in enumerate(xs):
        if c in dic:
            dic[c].append(i)

    # loop through possible starting point of the pattern

    for istart in dic[p[0]]:
        pos = []

        i = istart # the position of the current character
        pos.append(i)
        success = True # indicate whether a match is found
        # loop the remaining characters in the pattern
        for c in p[1:]:
            possible_choice  = list(filter(lambda t: t > i, dic[c])) # possible positions
            if possible_choice == []:
                success = False
                break
            else:
                i = min(possible_choice)
            pos.append(i)
        if success: # found a match
            matched.append(pos)

    return  sorted(matched,key=lambda x: x[-1]-x[0])[0] # return the shortest match
