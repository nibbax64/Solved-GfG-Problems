def xor_arr(array, n):
    ret = [0,0]
    for i in range(0, n-1):
        ret[0] = ret[0]^array[i]
        ret[1] = ret[1]^(i+1)
#        print(ret)
    ret[1] = ret[1]^(i+1)
#    print(ret)
    return ret
#-----XOR---
def missing_number_in_array(array, n):
    ip_arr,n_arr = xor_arr(array, n)
    return (ip_arr^n_arr)-1

'''
#---Sum Method---
def missing_number_in_array(array, n):
    sum_ = (n * (n+1))/2
    return (sum_ - sum(array))
#---data type overflow issues(C,Java)---
'''
if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        n = int(input())
        array = tuple(map(int, input().split()))

        print(":: ",missing_number_in_array(array, n))
'''
2
5
1 2 3 5
10
1 2 3 4 5 6 7 8 10

'''
