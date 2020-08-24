class Backtracking_SUDOKU:
    def __init__(self, board):
        self.board = board

    def solve_the_sudoku(self):

if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        ini_board = []
        for _ in range(9):
            ini_board.append(list(map(int, input().split())))
        obj = Backtracking_SUDOKU(ini_board)
        #obj = Backtracking_NQ_BFS(ip)
        obj.solve_the_sudoku(0)
        print()

'''
1
3 0 6 5 0 8 4 0 0
5 2 0 0 0 0 0 0 0
0 8 7 0 0 0 0 3 1
0 0 3 0 1 0 0 8 0
9 0 0 8 6 3 0 0 5
0 5 0 0 9 0 6 0 0
1 3 0 0 0 0 2 5 0
0 0 0 0 0 0 0 7 4
0 0 5 2 0 6 3 0 0

'''
