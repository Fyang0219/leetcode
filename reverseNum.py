def reverseInt(num):
    answer = 0
    sign = 1 if num > 0 else -1
    num = abs(num)
    while num > 0:
        answer = answer * 10 + num % 10
        num /= 10
    
    print(answer * sign)


reverseInt(11567)