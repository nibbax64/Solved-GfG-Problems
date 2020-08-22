from Tree import Node

def get_VerticalOrder(root, hd, hash_map):

    if root == None:
        return

    try:
        hash_map[hd].append(root.data)
    except:
        hash_map[hd] = [root.data]

    get_VerticalOrder(root.left, hd-1, hash_map)
    get_VerticalOrder(root.right, hd+1, hash_map)

def bottom_view_of_binary_tree(root):
    hash_map = dict()
    to_return = []

    get_VerticalOrder(root, 0, hash_map)

    #hash_map =
    for key,value in enumerate(sorted(hash_map)):
        to_return.append(hash_map[value][-1])

    return to_return

user_ip = (
    "root = Node(20)\nroot.left = Node(8)\nroot.right = Node(22)\nroot.left.left = Node(5)\nroot.left.right = Node(3)\nroot.right.left = Node(4)\nroot.right.right = Node(25)\nroot.left.right.left = Node(10)\nroot.right.left.right = Node(14)",
    "root = Node(3)\nroot.left = Node(1)\nroot.right = Node(2)",
    "root = Node(10)\nroot.left = Node(20)\nroot.right = Node(30)\nroot.left.left = Node(40)\nroot.left.right = Node(60)"
)
if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        n = int(input())
        #array = tuple(map(int, input().split()))
        root = None
        #root = Node.insertL(array, None, 0, n)
        exec(user_ip[_])

        print(":: ",bottom_view_of_binary_tree(root))
        #print_VerticalOrder(root)
        #root.InOrder()
        print()

'''
3
8
3
5

8
         20
       /    \
      8     22
     / \    / \
    5   3  4   25
       /    \
      10     14
3
        3
       / \
      1   2
5
        10
       /  \
      20  30
     / \
    40 60
'''
