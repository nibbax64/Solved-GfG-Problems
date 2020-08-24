from LinkedList import LinkedList

def finding_middle_element_in_a_linked_list(start_ptr=None):
    fast = slow = start_ptr

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    return slow.data

if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        n = int(input())
        array = tuple(map(int,input().split()))

        start = LinkedList(array[0])
        ptr = start
        for i in range(1,n):
            ptr.next = LinkedList(array[i])
            ptr = ptr.next

        print(":: ",finding_middle_element_in_a_linked_list(start))

'''
2
5
1 2 3 4 5
6
2 4 6 7 5 1

'''
