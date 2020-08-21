#----------------------------------------------
#-----------------O(n^2)-----------------------
#----------------------------------------------
def count_the_triplets(array, n):
    array.sort()
    count = 0

    for i in range(n-1, 1, -1):
        sum_ = array[i]
        j,k = 0,i-1
        while(j < k):
            temp = array[j]+array[k]
            if temp == sum_:
                count += 1
                if array[j]==array[j+1]:
                    j += 1
                    k += 1
                k -= 1
            elif temp > sum_:
                k -= 1
            else:
                j += 1

    if count == 0:
        return -1
    else:
        return count

if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        n = int(input())
        array = list(map(int, input().split()))

        print(":: ",count_the_triplets(array, n))

'''
3
4
1 5 3 2
3
3 2 7
6
4 3 1 3 3 4

'''
