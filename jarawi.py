# numpy and scipy are available for use
import numpy as np
import scipy

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
    return next(input_parser, "end")

def get_number():
    s = np.fromiter(get_word())
    reversedString = s[::-1]
    while True:
        data = get_word()
        if data == "end":
            break
        else:
            if data.length()>1:
                for i in range(data.length()):
                    suffix += data[i]
                    if suffix in reversedString[0:4]:
                        count += count
            
    try:
        return int(count)
    except ValueError:
        return float(count)


a = get_number()
b = get_number()

res = a + b
print(res)