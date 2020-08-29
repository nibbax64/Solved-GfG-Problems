def partition(array, low, high):
    i = low-1
    pivot = array[high]

    for j in range(low, high):
        if(array[j] < pivot):
            i = i+1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]

    return i+1

def sort_it(array, low, high):
    if(low < high):
        p = partition(array, low, high)
        sort_it(array, low, p-1)
        sort_it(array, p+1, high)

    return array

def merge_without_extra_space(array1, array2, n1, n2):
    for i in range(n1):
        for j in range(n2):
            if array1[i] > array2[j]:
                array1[i],array2[j] = array2[j],array1[i]

    array2 = sort_it(array2, 0, n2-1)
    return "{},{}".format(str(array1), str(array2))

if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        n1, n2 = input().split()
        n1, n2 = int(n1), int(n2)
        array1 = list(map(int, input().split()))
        array2 = list(map(int, input().split()))

        print(":: ",merge_without_extra_space(array1, array2, n1, n2))

'''
4
1 2
10
2 3
6 4
1 5 9 10 15 20
2 3 8 13
4 5
1 3 5 7
0 2 6 8 9
2 3
10 12
5 18 20

'''
