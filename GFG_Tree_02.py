from Tree import Node

def check_for_bst(root, l=None, r=None):
    if root == None:
        return True
    if l != None and root.data <= l.data:
        return False
    if r != None and root.data >= r.data:
        return False

    return (check_for_bst(root.left, l, root) and check_for_bst(root.right, root, r))

user_ip = (
    "root = Node(2)\nroot.left = Node(1)\nroot.right = Node(3)",
    "root = Node(2)\nroot.right = Node(7)\nroot.right.right = Node(6)\nroot.right.right.right = Node(5)\nroot.right.right.right.right = Node(9)\nroot.right.right.right.right.right = Node(2)\nroot.right.right.right.right.right.right = Node(6)"
)

if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        n = int(input())
        #array = tuple(map(int, input().split()))
        root = None
        #root = Node.insertL(array, None, 0, n)
        exec(user_ip[_])

        print(":: ",check_for_bst(root))
        #root.InOrder()
        #print()

'''
2
3
7

3
  2
 / \
1   3
7
7
2
 \
  7
   \
    6
     \
      5
       \
        9
         \
          2
           \
            6

'''
