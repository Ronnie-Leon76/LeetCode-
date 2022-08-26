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
#import numpy
#import scipy

t = get_number()
if t>=1 and t<=25:
    for i in range(t):
        c = get_number()  
        n = get_number()
        if c>=1 and c<=500 and n>=1 and n<=200:
            for p in range(1,n+1):
                w = get_number()
                f = get_number()
                if w>=1 and w<=100 and f>=1 and f<=1000:
                    if p>1:
                        weight += w
                    else:
                        weight = w
                    if weight<=c:
                        if p>1:
                            power += f
                        else:
                            power = f
            print(power)
 
          
      


