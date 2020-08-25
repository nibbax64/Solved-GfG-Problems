#---:TODO:manacher's algorithm---

#---Dynamic----
def longest_palindrome_in_a_string(string, size):
    dyn_map = [[False for i in range(size)] for j in range(size)]
    start, end = 0,1
    #----len_1---
    for i in range(0, size):
            dyn_map[i][i] = True
    #----len_2---
    for i in range(0, size-1):
        if string[i]==string[i+1]:
            dyn_map[i][i+1] = True
            start, end = i,i+2
    #----len_n---
    for i in range(2, size):
        for j in range(0, size-i):
            if string[j]==string[j+i] and dyn_map[j+1][j+i-1]==True:
                dyn_map[j][j+i] = True
                start, end = j, j+i+1

    return string[start:end]

if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        string = input()
        print(":: ", longest_palindrome_in_a_string(string, len(string)))

'''
3
aaaabbaa
geeksforgeeks
cdcabcdcbaccd

'''
'''
    a  a  a  a  b  b  a  a
    0  1  2  3  4  5  6  7
a 0 [1][1][1][1][x][x][x][x]
a 1 [0][1][1][1][x][x][x][x]
a 2 [0][0][1][1][x][x][x][1]
a 3 [0][0][0][1][x][x][1][x]
b 4 [0][0][0][0][1][1][x][x]
b 5 [0][0][0][0][0][1][x][x]
a 6 [0][0][0][0][0][0][1][1]
a 7 [0][0][0][0][0][0][0][1]
'''
