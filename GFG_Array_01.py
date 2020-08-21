#----------------------------------------------
#---------Sliding Window-----------------------
#----------------------------------------------
def subarray_with_given_sum(array, n, sum_):

    window, window_h, window_sum, flag = [], 0, 0, False
    for i in range(n):
        window.append(array[i])
        window_sum = sum(window)
        while window_sum > sum_:
            window_sum -= array[window_h]
            window_h += 1
        if window_sum == sum_:
            flag = True
            break
    if flag == False:
        return -1
    else:
        return (window_h+1, i+1)


if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        n, sum_ = input().split()
        n, sum_ = int(n), int(sum_)
        array = tuple(map(int, input().split()))

        print(":: ",subarray_with_given_sum(array, n, sum_))
