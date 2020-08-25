op = []
def permutations_of_a_given_string(array, left, right):
    if left==right:
        op.append("".join(array))
    else:
        for i in range(left, right+1):
            #---Swap ini and pos---
            array[left], array[i] = array[i], array[left]
            permutations_of_a_given_string(array, left+1, right)
            #---Swap ini and pos back to place---
            array[left], array[i] = array[i], array[left]
    return

if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        string = list(input())
        op = []
        permutations_of_a_given_string(string, 0, len(string)-1)
        print(":: ", op)

'''
2
ABC
ABSG

'''
