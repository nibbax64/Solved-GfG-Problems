from LinkedList import LinkedList

def print_list(start):
    if start == None:
        return "Null"
    else:
        return f"{start.data}->{print_list(start.next)}"

def rotate_a_linked_list(start_prt, n):
    ptr1, ptr2 = start_prt, None

    while n>1:
        ptr1 = ptr1.next
        n -= 1
    #print(print_list(ptr1))
    ptr2 = ptr1
    while ptr1.next!=None:
        ptr1 = ptr1.next
    #print(print_list(ptr1))
    ptr1.next = start_prt

    start_prt = ptr2.next
    ptr2.next = None

    return start_prt



if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        n = int(input())
        array = tuple(map(int,input().split()))
        k = int(input())

        start = LinkedList(array[0])
        ptr = start
        for i in range(1,n):
            ptr.next = LinkedList(array[i])
            ptr = ptr.next

#        print(":: ",print_list(start))
        start = rotate_a_linked_list(start, k)
        print(":: ",print_list(start))

'''
2
8
1 2 3 4 5 6 7 8
4
5
2 4 7 8 9
3

'''
