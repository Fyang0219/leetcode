def reverseStr(str):
    s = list(str)
    for i in xrange(0, len(s)/2):
        tmp = s[i]
        s[i] = s[len(s)-1-i]
        s[len(s)-1-i] = tmp

    print(''.join(s))


reverseStr('fasri43gnvr3ign')