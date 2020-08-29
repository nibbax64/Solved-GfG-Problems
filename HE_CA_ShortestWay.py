'''
The statement of this problem is quite short , apt and clear.
We don't want any coder to spend time in reading a lengthy, boring story that has no connection with the actual problem.

The problem states:
Given a pair (1,1), your aim is to get a new pair (a,b) in minimum number of operations.
There are two types of operations you can use:
1.) If the pair is ( x , y ) then change it to ( x+y, y )
2.) If the pair is ( x , y ) then change it to ( x, x+y )
It is guaranteed that a and b are co-prime .

Input:
The first line contains the number of test cases T. Then, T lines follow, where each line contains a and b respectively.

Output:
Print a line containing the minimum number of operations required to achieve the given fraction, corresponding to each test case.

Constraints:
1 <= T <=10
1<= a,b <=10^18
a and b are co-primes

SAMPLE INPUT
2
1 1
5 2

SAMPLE OUTPUT
0
3
'''
import time

INT_MAX = 10**18 - 1
def func_DFS(to_, x,y, level):
    if x==to_[0] and y==to_[1]:
        return level
    elif x>to_[0] or y>to_[1]:
        return INT_MAX
    else:
        return min(func_DFS(to_, x+y, y, level+1), func_DFS(to_, x, x+y, level+1))

def func_BFS(to_):
    q = []
    #i = 0
    data = [(1,1,0)]
    while True:
        #i += 1
        q.extend(data)
        #input()
        #print(f"{i} | {q}")
        data = q.pop(0)
        if data[0]==to_[0] and data[1]==to_[1]:
            level = data[2]
            break
        else:
            data = [(data[0]+data[1], data[1], data[2]+1), (data[0], data[0]+data[1], data[2]+1)]

    return level


if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        to_ = tuple(map(int, input().split()))

        print(to_)
        start = time.time()
        print(f"{func_DFS(to_,1,1,0)}",end="| ")
        end = time.time()
        tt = (end-start)*10**3
        if(tt<1000):
            print("DFS : {:.12f} ms".format(tt))
        else:
            print("DFS : TE")

        start = time.time()
        print(f"{func_BFS(to_)}",end="| ")
        end = time.time()
        tt = (end-start)*10**3
        if(tt<1000):
            print("BFS : {:.12f} ms".format(tt))
        else:
            print("BFS : TE")

'''
2
1 1
5 2

11
94 79
40 7
58 53
37 6
43 23
87 46
91 27
43 5
442 105
106 13
3 2


9
66 5
80 53
366 169
425 183
873 686
675 287
354 305
316 251
564 415

'''
