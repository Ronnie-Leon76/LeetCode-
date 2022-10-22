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
#import scipy
class Node:
    def __init__(self, weight):
        self.left = None
        self.weight = weight
        self.right = None

class Tree:
    def createNode(self, weight):
        return Node(weight)
    def insert(self, node, weight):
        if node is None:
            return self.createNode(weight)
        if data<node.weight:
            node.left = self.insert(node.left, weight)
        elif data>node.weight:
            node.right = self.insert(node.right, weight)
        return node
    def traverseInOrder(self, root, W):
        if root is not None:
            self.traverseInOrder(root.left)
            if(root.weight>=)
            self.traverseInOrder(root.right)
        
    

T = get_number()
N = get_number()
W = numpy.zeros(N)
root = None
tree = Tree()
for i in range(T):
    for j in range(N):
        W[j] = get_number()
    root = tree.insert(root, W[0])
    for m in range(1,N+1):
        tree.insert(root,W[m])
    mat = numpy.zeros(N-1,2)
    for k in range(N-1):
        for m in range(2):
            mat[k][m] = get_number()
    Q = get_number()
    mat1 = numpy.zeros(Q,3)
    for n in range(Q):
        for r in range(3):
            mat1[n][r] = get_number()
    x, y = mat1.shape
    for p in range(x):
        for q in range(y):
            if mat[p][0] == 1:
                if mat[p][1]>=1 and mat[p][1]<=N and mat[p][2]>=1 and mat[p][2]<=1000000000:
                    
                    
                    
        