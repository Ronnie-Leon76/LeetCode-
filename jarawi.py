# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0 and len(number) < 1000000:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    # Value error if a string is passed    
    except ValueError:
        return data

# numpy and scipy are available for use
# import numpy
# import scipy

s = get_number()
# s_len = len(s)
# number of letters of the suffix
# implementation of the ceil() method using -(7//-2) syntax
# suffix_number_letters = -(s_len//-2)
# slicing s to obtain its suffix
# suffix_s = s[-suffix_number_letters:]
q = int(get_number())
if q>=1 and q<=50000:
    count = 0
    for i in range(1, q+1):
        p = get_number()
        p_len = len(p)
        for j in range(1, p_len+1):
            if j<=1:
                substr = p[-j:0]
            else:
                substr += p[-j:0]
            if substr in s:
                count += 1
    print(count)
            
                


