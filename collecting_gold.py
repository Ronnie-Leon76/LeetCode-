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
import numpy
# import scipy

def dijikstra(graph,start,goal)-> list:
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    while unseenNodes:
        minNode = None
        # ensure minNode is set to the Node with the least weight
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node]<shortest_distance[minNode]:
                minNode = node
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode]<shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
            
        unseenNodes.pop(minNode)
        currentNode = goal
        while currentNode != start:
            try:
                path.insert(0, currentNode)
                currentNode = predecessor[currentNode]
            except KeyError:
                print("Path not reachable")
                break
        path.insert(0, start)
        if shortest_distance[goal] != infinity:
            # print("Shortest distance is: " + str(shortest_distance[goal]))
            # print("And the path is: " + str(path))
            return path
        

n = get_number()
if n>=1 and n<=20000:
    m = get_number()
    if m>=0 and m<=20000:
        ids = np.zeros(n)
        min = 0
        min = 0
        count = 0
        for i in range(n):
            min = ids[0]
            max = ids[0]
            ids[i] = get_number()
            if ids[i]<min:
                min = ids[i]
            elif ids[i]>max:
                max = ids[i]
        for j in range(m):
            graph = {}
            parentNode = str(get_number())
            childNode = str(get_number())
            weight = get_number()
            graph[parentNode] = [ childNode: weight ]
        shortest_path = dijikstra(graph, str(min), str(max))
        product = 1
        for i in shortest_path:
            for j in range(1, i+1):
                # Skip 1 as it is not a prime number
                # prime nor composite
                if j == 1:
                    continue
                # flag variable to tell
                # if 1 is prime or not
                flag = 1
                
                for k in range(2, j // 2 + 1):
                    if(j%k == 0):
                        flag = 0
                        break
                if flag == 1 and product<j:
                    count += 1
                    product *= j
            product = 1
        print(count)
                    
                
            
                    
                    
        
        
        
        
            
            
            
