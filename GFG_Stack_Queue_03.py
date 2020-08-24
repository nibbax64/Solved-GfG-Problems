def q_pop(stack_1, n):
    stack_2 = []
    for i in range(n):
        stack_2.append(stack_1[n-1-i])
    try:
        temp = stack_2.pop()
        n = len(stack_2)
        stack_1 = []
        for i in range(n):
            stack_1.append(stack_1[n-i-1])
    except:
        temp = -1
        stack_1 = []

    return (stack_1, temp)

def queue_using_two_stacks(array, n):
    stack_1 = []
    op = []

    for i in range(n):
        if array[i] == 1:
            i += 1
            stack_1.append(array[i])
            print(stack_1)
        elif array[i] == 2:
            tmp = q_pop(stack_1, len(stack_1))
            stack_1 = tmp[0]
            op.append(tmp[1])

    return op

if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        n = int(input())
        array = tuple(map(int, input().split()))
        print(":: ",queue_using_two_stacks(array, n))

'''
2
5
1 2 1 3 2 1 4 2
4
1 2 2 1 4

'''
