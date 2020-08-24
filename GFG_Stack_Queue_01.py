def parenthesis_checker(string):
    stack = []
    open, close = ('(', '[', '{'), (')', ']', '}')
    flag = True

    for i in string:
        #print(stack)
        if i in open:
            stack.append(i)
        elif i in close:
            if stack.pop() != open[close.index(i)]:
                flag = False
                break
        else:
            continue
    if len(stack) != 0:
        flag = False

    return flag

if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        string = input()
        print(":: ",parenthesis_checker(string))

'''
3
{([])}
()
([]

'''
