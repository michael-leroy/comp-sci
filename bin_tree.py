#!/usr/bin/python


#bin treez
import unittest




class Node(object):
    '''
    Creates a node object to be used by the BinTree class
    for constructing a Binary Tree.
    Args:
        new_key (int): Key value for the new node you are creating


    Attributes:
        key (int): Key value for node.
        left_child (int): Left child for new node.
        right_child (int): Right child for new node.
    '''
    def __init__(self, the_key):
        self.key = the_key
        self.left_child = None
        self.right_child = None




class BinTree(object):
    '''
    Creates a binary tree that when implmented properly
    should have the following run times::
        Average: O(log n)
        Worst: O(n)


    Args:
        new_node (int): Key value for root node on creation. 


    Attributes:
        root (node or none): The root of the binary tree.
    '''
    def __init__(self, new_root=None):
        if new_root:
            self.root = Node(new_root)
        else:
            self.root = None


    def search(self, key, node):
        '''
        Searches a well balanced binary tree in
        O(log N) otherwise O(n).


        Args:
            key (int): The key you wish to find in the tree.
            node (int): The node to start searching from.
                        Usually the root
        Returns:
            node: The node with specified key.
        '''
        if not node or node.key == key:
            return node
        if key < node.key:
            return self.search(key, node.left_child)
        else:
            return self.search(key, node.right_child)


    def _search_iter(self, key, node):
        '''
        Searches a well balanced binary tree in
        O(log N) otherwise O(n). Iterative version.


        Args:
            key (int): The key you wish to find in the tree.
            node (int): The node to start searching from.
                        Usually the root
        Returns:
            node: The node with specified key.
        '''
        current_node = node
        while current_node is not None:
            if current_node.key == key:
                return current_node
            elif key < current_node.key:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return None


    def add(self, node, new_key):
        if not self.root:
            self.root = Node(new_key)
        else:
            if new_key < node.key:
                if not node.left_child:
                    node.left_child = Node(new_key)
                else:
                    self.add(node.left_child, new_key)
            else:
                if not node.right_child:
                    node.right_child = Node(new_key)
                else:
                    self.add(node.right_child, new_key)


    def delete(self, node, key_to_find):
        '''
        Finds and a node with a key value of key_to_find
        Args:
            node (node): Node to start searching for deletion, usually 
            the root node.
            key_to_find (int): Key value of node you wish to delete
        '''
        pass


    def is_valid_binary_tree(self, root_node):
        '''
        Determines if a tree is a valid binary tree
        Args:
            root_node (node): Node of tree to check


        Returns:
            True if a valid binary tree, otherwise False.
        '''
        #print('called')
        if self.root is None:
            return False


        if self.root.left_child is None and self.root.right_child is None:
            return True


        if root_node.right_child is None and root_node.left_child is not None:
            if root_node.key < root_node.left_child.key:
                return False


            else:
                print('c\n')
                self.is_valid_binary_tree(root_node.left_child)


        elif root_node.left_child is None and root_node.right_child is not None:
            if root_node.key > root_node.right_child.key:
                return False


            else:
                self.is_valid_binary_tree(root_node.right_child)


        elif root_node.left_child is not None and root_node.right_child is not None:
            if root_node.left_child.key < root_node.right_child.key:
                self.is_valid_binary_tree(root_node.left_child)
                self.is_valid_binary_tree(root_node.right_child)
            else:
                return False


        #elif root_node.left_child.key > root_node.right_child.key:
        #    return False
        else:
            return True


    def invert_tree(self, node):
        if node is not None:
            self._invert_tree_helper(node)
    
    def _invert_tree_helper(self, node):
        '''
        Invert a tree for no reason because interviewers
        love to ask this question.
        With this funciton we will swap left/right children.
        Args:
            node (node): Node to start inverting from. Usually root node.


        Returns:
            Nothing, modifies self.root.
        '''
        if node.left_child is not None and node.right_child is not None:
            temp_left = Node(node.left_child.key)
            temp_left.left_child = node.left_child.left_child
            temp_left.right_child = node.left_child.right_child
            node.left_child = node.right_child
            node.right_child = temp_left
            self.invert_tree(node.left_child)
            self.invert_tree(node.right_child)


        elif node.left_child is not None and node.right_child is None:
            node.right_child = node.left_child
            node.left_child = None
            self.invert_tree(node.right_child)


        else:        
            node.left_child = node.right_child
            node.left_child = None
            self.invert_tree(node.left_child)            


    def get_tree_height(self, node):
        '''
        Returns the height of a binary tree with this assumption
        An empty tree is -1.
        A tree with only a root node is 0.
        A tree with a root node and at least a single child is 1.
        Args:
            node (node): Node to start counting with. Usually a root node.


        Returns:
            int: the height of the tree.
        '''
        if not self.root:
            return -1


        if node.left_child is None and node.right_child is None:
            return 0


        if not node.left_child:
            return 1 + self.get_tree_height(node.right_child)


        elif not node.right_child:
            return 1 + self.get_tree_height(node.left_child)


        else:
            return 1 + max(self.get_tree_height(node.left_child),
                self.get_tree_height(node.right_child))




class TestBinTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinTree()


    def tearDown(self):
        self.tree = None


    def test_tree_add_into_root(self):
        self.tree.add(self.tree.root, 5)
        self.assertEqual(self.tree.root.key, 5)


    def test_tree_add_element_to_left(self):
        self.tree.add(self.tree.root, 4)
        self.tree.add(self.tree.root, 2)
        self.assertEqual(self.tree.root.left_child.key, 2)


    def test_tree_add_element_to_right(self):
        self.tree.add(self.tree.root, 4)
        self.tree.add(self.tree.root, 2)
        self.tree.add(self.tree.root, 6)
        self.assertEqual(self.tree.root.right_child.key, 6)


    def test_tree_search(self):
        self.tree.add(self.tree.root, 4)
        self.tree.add(self.tree.root, 2)
        self.tree.add(self.tree.root, 6)
        self.tree.add(self.tree.root, 11)
        self.tree.add(self.tree.root, 8)
        self.tree.add(self.tree.root, 22)
        self.tree.add(self.tree.root, 1)
        self.tree.add(self.tree.root, 99)
        self.tree.add(self.tree.root, 5)
        result = self.tree.search(5, self.tree.root)
        self.assertEqual(result.key, 5)
        result = self.tree.search(199, self.tree.root)
        self.assertIsNone(result)
        result = self.tree.search(11, self.tree.root)
        self.assertEqual(result.key, 11)


    def test_tree_search(self):
        self.tree.add(self.tree.root, 4)
        self.tree.add(self.tree.root, 2)
        self.tree.add(self.tree.root, 6)
        self.tree.add(self.tree.root, 11)
        self.tree.add(self.tree.root, 8)
        self.tree.add(self.tree.root, 22)
        self.tree.add(self.tree.root, 1)
        self.tree.add(self.tree.root, 99)
        self.tree.add(self.tree.root, 5)
        result = self.tree.search(5, self.tree.root)
        self.assertEqual(result.key, 5)
        result = self.tree.search(199, self.tree.root)
        self.assertIsNone(result)
        result = self.tree.search(11, self.tree.root)
        self.assertEqual(result.key, 11)


    def test_tree_height_empty_tree(self):
        result = self.tree.get_tree_height(self.tree.root)
        self.assertEqual(result, -1)


    def test_tree_height_only_root(self):
        self.tree.add(self.tree.root, 5)
        result = self.tree.get_tree_height(self.tree.root)
        self.assertEqual(result, 0)


    def test_tree_height_two_deep(self):
        self.tree.add(self.tree.root, 4)
        self.tree.add(self.tree.root, 2)
        self.tree.add(self.tree.root, 5)
        self.tree.add(self.tree.root, 6)
        result = self.tree.get_tree_height(self.tree.root)
        self.assertEqual(result, 2)


    def test_tree_height_ten_deep(self):
        self.tree.add(self.tree.root, 17)
        self.tree.add(self.tree.root, 5)
        self.tree.add(self.tree.root, 4)
        self.tree.add(self.tree.root, 2)
        self.tree.add(self.tree.root, 3)
        self.tree.add(self.tree.root, 18)
        self.tree.add(self.tree.root, 19)
        self.tree.add(self.tree.root, 20)
        self.tree.add(self.tree.root, 21)
        self.tree.add(self.tree.root, 22)
        self.tree.add(self.tree.root, 23)
        self.tree.add(self.tree.root, 50)
        self.tree.add(self.tree.root, 51)
        self.tree.add(self.tree.root, 52)
        self.tree.add(self.tree.root, 53)
        result = self.tree.get_tree_height(self.tree.root)
        self.assertEqual(result, 10) 


    def test_tree_valid_function_root_only(self):
        self.tree.add(self.tree.root, 17)
        result = self.tree.is_valid_binary_tree(self.tree.root)
        self.assertTrue(result)


    def test_tree_valid_function_empty_expect_false(self):
        result = self.tree.is_valid_binary_tree(self.tree.root)
        self.assertFalse(result)


    #def test_tree_valid_function_expect_true(self):
    #    self.tree.add(self.tree.root, 17)
    #    self.tree.add(self.tree.root, 5)
    #    self.tree.add(self.tree.root, 4)
    #    self.tree.add(self.tree.root, 2)
    #    result = self.tree.is_valid_binary_tree(self.tree.root)
    #    self.assertTrue(result)


    def test_invert_tree(self):
        self.tree.add(self.tree.root, 7)
        self.tree.add(self.tree.root, 10)
        self.tree.add(self.tree.root, 5)
        self.tree.add(self.tree.root, 9)
        self.tree.add(self.tree.root, 11)
        self.tree.add(self.tree.root, 3)
        self.tree.add(self.tree.root, 4)
        self.assertEqual(self.tree.root.key, 7)
        self.assertEqual(self.tree.root.left_child.key, 5)
        self.assertEqual(self.tree.root.right_child.key, 10)
        self.tree.invert_tree(self.tree.root)
        self.assertEqual(self.tree.root.left_child.key, 10)
        self.assertEqual(self.tree.root.right_child.key, 5)




if __name__ == "__main__":
    unittest.main()

