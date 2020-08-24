class Backtracking_NQ:
    def __init__(self, size):
        self.size = size
        self.board = [0]*size

def print_board(board, size):
    print("::")
    for i in range(0, size):
        for j in range(0, size):
            if(board[i] == j):
                print("[Q]",end="")
            else:
                print("[ ]",end="")
        print()
    print()

class Backtracking_NQ_DFS(Backtracking_NQ):
    def is_safe(self, x, y):
        for i in range(0, x):
            if self.board[i]==y or abs(i-x)==abs(self.board[i]-y):
                return False
        return True

    def n_queen_problem(self, x):
        for i in range(0, self.size):
            if self.is_safe(x, i):
                self.board[x] = i
                if x == self.size-1:
                    print_board(self.board, self.size)
                self.n_queen_problem(x+1)

if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        ip = int(input())
        obj = Backtracking_NQ_DFS(ip)
        #obj = Backtracking_NQ_BFS(ip)
        obj.n_queen_problem(0)
        print()

'''
7
1
2
3
5
8
13
21

'''
