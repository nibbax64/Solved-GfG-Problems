class Node:

    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def insertL(arr, root, i, n):
        if i < n:
            temp = Node(arr[i])
            root = temp

            root.left = Node.insertL(arr, root.left, 2*i+1, n)
            root.right = Node.insertL(arr, root.right, 2*i+2, n)

        return root

    def InOrder(self):
        if self.left:
            self.left.InOrder()
        print(self.data,end=" ")
        if self.right:
            self.right.InOrder()

    def PreOrder(self):
        print(self.data,end=" ")
        if self.left:
            self.left.PreOrder()
        if self.right:
            self.right.PreOrder()

    def PostOrder(self):
        if self.left:
            self.left.PostOrder()
        if self.right:
            self.right.PostOrder()
        print(self.data,end=" ")

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

    def get_VerticalOrder(root, hd, hash_map):

        if root == None:
            return

        try:
            hash_map[hd].append(root.data)
        except:
            hash_map[hd] = [root.data]

        get_VerticalOrder(root.left, hd-1, hash_map)
        get_VerticalOrder(root.right, hd+1, hash_map)

    def print_VerticalOrder(root):

        hash_map = dict()
        hd = 0
        get_VerticalOrder(root, hd, hash_map)

        hash_map = enumerate(sorted(hash_map))
        for key,value in hash_map:
            print(hash_map[value])


class BinNode(Node):

    def insert(self, data):
        if self.data:
            # left leaf
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            # right leaf
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
