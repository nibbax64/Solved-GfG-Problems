def next_larger_element(array, n):
    stack, temp = [], []

    stack.append(array[0])
    for i in range(1, n):
        if len(array) == 0:
            stack.append(array[i])
            continue
        while len(stack) != 0 and stack[-1] < array[i]:
            temp.append(array[i])
            stack.pop()
        stack.append(array[i])

    while len(stack) != 0:
        temp.append(-1)
        stack.pop()

    return temp


if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        n = int(input())
        array = tuple(map(int, input().split()))
        print(":: ",next_larger_element(array, n))

'''
2
4
1 3 2 4
4
4 3 2 1

'''
