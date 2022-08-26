def solution(X,Y,colors):
    redCount = 0
    greenCount = 0
    n = len(X or Y)
    x = len(colors)
    for i in range(x):
        if colors[i:i+1] == 'R':
            redCount += 1
        elif colors[i:i+1] == 'G':
            greenCount += 1
    count = 0
    zeroCount = 0
    while count < n:
        if X[n] == 0 or Y[n] == 0:
          zeroCount += 1
        count += 1
    if(redCount == greenCount):
        if(zeroCount != n):
            return redCount + greenCount
    elif(redCount != greenCount):
        least = 0
        if(redCount<greenCount):
            least = redCount
            return least*2
        else:
            least = greenCount
            return least*2

      
        