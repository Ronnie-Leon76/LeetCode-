# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
# import numpy
# import scipy
t = get_number()
if t>=1 and t<=25:
    for i in range(1, t+1):
        n = get_number()
        max_sum = 0
        sequence = []
        for j in range(1, n+1):
            a = get_number()
            sequence.append(a)
            a += 1
            max_sum += a
        # seq_len = len(sequence)
        # new_sequence = [sequence[i] for i in range(1, seq_len+1)]
        print(max_sum)
        print(sequence)
            

