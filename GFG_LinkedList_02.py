from LinkedList import LinkedList

def print_list(start=None):
    if start == None:
        return "Null"
    elif start.next == None:
        return f"{start.data}"
    else:
        return f"{start.data}->{print_list(start.next)}"

def reverse_a_linked_list(start_ptr=None):
    slider1 = start_ptr
    slider2, slider3 = None, None

    while slider1 != None:
        slider3 = slider2
        slider2 = slider1
        slider1 = slider1.next
        slider2.next = slider3

    return slider2

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

        start = reverse_a_linked_list(start)

        print(":: ",print_list(start))
