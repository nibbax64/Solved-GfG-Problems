from Tree import Node

def get_LevelOrder(root, level, hash_array):

    if root == None:
        return

    if hash_array[level] == None:
        hash_array[level] = root.data
    else:
        pass

    if hash_array[-1] == None:
        hash_array[-1] = level
    else:
        if hash_array[-1] < level:
            hash_array[-1] = level

    get_LevelOrder(root.left, level+1, hash_array)
    get_LevelOrder(root.right, level+1, hash_array)

def left_view_of_binary_tree(root):
    hash_array = [None]*10
    get_LevelOrder(root, 0, hash_array)

    hash_array = hash_array[:hash_array[-1]+1]

    return hash_array

if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        n = int(input())
        array = tuple(map(int, input().split()))
        root = Node.insertL(array, None, 0, n)

        print(":: ",left_view_of_binary_tree(root))

        #print()

'''
3
8
1 2 3 4 5 6 7 8
3
1 3 2
5
10 20 30 40 60

        1
       / \
      2   3
     / \ / \
    4  5 6  7
   /
  8
'''
