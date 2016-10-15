# Name: Chiu Ming Abraham Tsang
# On my honor as a University of Colorado Student, this code was entirely written by myself with no unauthorized help.

# This class implements a Binary Search Tree Class
# The binary search tree class will include functionality of
#   1. Insert a Node in the Tree.
#   2. Search for a Node in the Tree
#   3. Various traversals including in order, preorder and postorder traversals.
#
#  The binary search tree is made of class Node objects.
#    Each node has three members: key is an integer, left and right child point to nodes.
#    If left is None, then it means that the node has no left child.
#    If right is None then the node has no right child.


class Node:

    def __init__(self, my_key): # Constructor for the Node.
        self.key = my_key       # Set the key to my_key
        self.left = None        # Set left child to None
        self.right = None       # Set right child to None

    def insert(self, key_to_insert):
        # TODO: write an insert function for the BST.
        # NOTE: If key_to_insert equals my_key,
        #       then the node need should NOT be inserted in the tree.
        # REMOVE the assert below
        if key_to_insert == self.key:
            return 0
        elif self.key == None:
            self.key = key_to_insert
        elif key_to_insert < self.key:
            if self.left != None:
                self.left.insert(key_to_insert)
            else:
                self.left = Node(None)
                self.left.insert(key_to_insert)
        elif key_to_insert > self.key:
            if self.right != None:
                self.right.insert(key_to_insert)
            else:
                self.right = Node(None)
                self.right.insert(key_to_insert)

			

    def inorder_traversal(self, ret_list):
        # TODO: write an inorder traversal function for the BST.
        # REMOVE the assert below
        if self != None:
            if self.left != None:
                self.left.inorder_traversal(ret_list)
            ret_list.append(self.key)
            if self.right != None:
                self.right.inorder_traversal(ret_list)
            
            return ret_list
        

    def get_depth(self):
        # TODO: write a get_depth function for the BST
        #   Depth of a tree with no children is 1.
        #   Otherwise, depth = 1 + max(depth(left subtree), depth(right subtree))
        # REMOVE the assert below
        if self.left == None and self.right == None:
            return 1
        elif self.left == None and self.right != None:
            return 1 + self.right.get_depth()
        elif self.right == None and self.left != None:
            return 1 + self.left.get_depth()
        else:
            return 1 + max(self.left.get_depth(), self.right.get_depth())

    def key_exists(self, key_to_find):
        # return True if the key_to_find is already in the tree,
        #   otherwise return False
        # REMOVE the assert below
        if key_to_find == self.key:
            return True
        elif key_to_find < self.key:
            if self.left != None:
                return self.left.key_exists(key_to_find)
            else:
                return False
        elif key_to_find > self.key:
            if self.right != None:
                return self.right.key_exists(key_to_find)
            else:
                return False
               

if __name__ == '__main__':
    print('Please do not call this file directly.')
    print('To run autograder script: please call the test_bst.py')
