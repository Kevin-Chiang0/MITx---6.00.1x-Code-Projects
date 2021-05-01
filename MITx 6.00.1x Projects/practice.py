def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    test = 0
    if a < b:
        test = a
    else:
        test = b
    while a % test != 0 or b % test != 0:
        print("hi")
        test -= 1
    return test

print(gcdIter(200,300))

