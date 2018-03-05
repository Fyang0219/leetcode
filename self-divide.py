
def selfdivide(left, right):

    result = []
    while left <= right:
        if '0' in str(left):
            left += 1
            continue
        else:
            skip = False
            for i in str(left):
                
                if left % int(i) != 0:
                    
                    left += 1
                    skip = True
                    break
            if skip == False : 
                result.append(left)
                left += 1
    print result
    return
selfdivide(1,22)