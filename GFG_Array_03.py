def kadane_algorithm(array, n):
    local_sum, global_sum = array[0], array[0]
    for i in range(1, n):
        local_sum = max(array[i], local_sum+array[i])
        global_sum = max(global_sum, local_sum)
    return global_sum

if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        n = int(input())
        array = tuple(map(int, input().split()))

        print(":: ",kadane_algorithm(array, n))

'''
2
5
1 2 3 -2 5
4
-1 -2 -3 -4

'''
