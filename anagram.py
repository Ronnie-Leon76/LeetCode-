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



strs = []   
strs_dict = {}
for i in range(n):
    n = get_number()
    strs.append(n)

for j in strs:
    charList = [0]*26
    charList[(ord(k) - ord('a'))] += 1
    if tuple(charList) in strs_dict:
        strs_dict[tuple(charList)].append(i)
    else:
        strs_dict[i] = {tuple(charList) : [i]}
size = 0
for k in range(len(strs_dict)):
    if len(strs_dict[k].values)>size:
        size = len(strs_dict[k].values)

print(size)
    
        
    

