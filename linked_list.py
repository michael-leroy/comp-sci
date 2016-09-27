#!/bin/python


import unittest


class Node(object):
    '''
    Creates a node object to be used by the Linked List class.
    '''
    def __init__(self,data=None, next_node=None):
        self.data = data
        self.next_node = next_node


    def get_data(self):
        return self.data


    def get_next(self):
        if self.next_node:
            return self.next_node


    def set_next_node(self, new_node):
        self.next_node = new_node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head


    def insert(self, data, index):
        '''
        Inserts node into the LL. If index 0 is used the running time is
        O(1), if not it is at worst case O(n)
        '''
        new_node = Node(data)
        if index == 0:
            new_node.set_next_node(self.head)
            self.head = new_node
            return None
        
        insert_after = self.access(index - 1)
        if insert_after and insert_after.next_node:
            insert_before = insert_after.get_next()
            insert_after.next_node = new_node
            new_node.next_node = insert_before
            return None
        elif insert_after and not insert_after.next_node:
            insert_after.next_node = new_node
            return None
        else:
            return None


    def delete(self, index):
        '''
        Deletes the first node in the linked list.
        O(1) run time if first index, O(n) otherwise.
        '''
        if index == 0:
            if self.head:
                self.head = self.head.get_next()
                return None


        before_node_delete = self.access(index - 1)
        if before_node_delete and before_node_delete.next_node:
            node_to_delete = before_node_delete.get_next()
            node_to_link_after_delete = node_to_delete.get_next()
            before_node_delete.next_node = node_to_link_after_delete
            node_to_delete = None
            return None
        elif before_node_delete and not before_node_delete.next_node:
            node_to_delete = before_node_delete.get_next()
            before_node_delete.next_node = None
            node_to_delete = None
            return None
        else:
            return None


    def access(self, index):
        '''
        Finds a node based on an index number for O(n) run time.
        Raises index error if nothing is found.
        '''
        current = self.head
        count = 0
        while current:
            if index == count and self.head:
                return current
            current = current.get_next()
            count += 1
        raise IndexError('LinkedList index out of range.')


    def access_data(self, index):
        '''
        Finds an item and returns the data. O(n) time.
        '''
        return self.access(index).data


    def size(self):
        '''
        Returns size of linked list. O(n) run time.
        '''
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def reverse(self, node, prev_node=None):
        '''
        Reverses the linked list in place.
        Trickyyyy
        '''
        if node.next_node is None:
            self.head = node
            node.next_node = prev_node
            return
        elif prev_node is None:
            print('called')
            node.next_node = self.reverse(node.next_node, node)
        else:
            temp_next_node = node.next_node
            node.next_node = prev_node
            self.reverse(temp_next_node, node)



class TestLinkedListMethods(unittest.TestCase):


    def setUP(self):
        self.node = Node()
        self.ll = LinkedList()


    def tearDown(self):
        self.node = None
        self.ll = None


    def test_node_instance(self):
        '''
        Test if Node creation is correct instance.
        '''
        a_node = Node()
        self.assertIsInstance(a_node, Node)


    def test_node_creation(self):
        '''
        Tests if the Node class work as expected.
        '''
        a = Node(data='foo')
        self.assertEqual(a.get_data(), 'foo')


    def test_node_linking(self):
        '''
        Tests is nodes are linked properly by the next_node property.
        '''
        b = Node(data='bar')
        a = Node(data='foo', next_node=b)
        self.assertIs(a.next_node, b)
        self.assertIsNot(b.next_node, a)
        self.assertIs(b.next_node, None)


    def test_ll_creation(self):
        '''
        Test if LinkedList call is a proper instance of LinkedList.
        '''
        a = LinkedList()
        self.assertIsInstance(a, LinkedList)


    def test_ll_insert_func_runs_without_crashing(self):
        '''
        Test if the insert function works without crashing.
        '''
        a = LinkedList()
        a.insert('foo', 0)
        self.assertEqual(a.insert('foo', 0), None)


    def test_ll_insert_first_position(self):
        '''
        Test the insert function in the first position.
        '''
        a = LinkedList()
        a.insert('foo', 0)
        self.assertEqual(a.access_data(0), 'foo')
        a.insert('bar', 0)
        self.assertEqual(a.access_data(0), 'bar')


    def test_ll_insert_third_position(self):
        '''
        Test the insert function in the third position.
        '''
        a = LinkedList()
        a.insert('foo', 0)
        a.insert('bar', 1)
        a.insert('jazzhands', 2)
        a.insert('spam', 2)
        self.assertEqual(a.access_data(0), 'foo')
        self.assertEqual(a.access_data(1), 'bar')
        self.assertEqual(a.access_data(2), 'spam')
        self.assertEqual(a.access_data(3), 'jazzhands')


    def test_ll_size_func(self):
        '''
        Test the size/length function.
        '''
        a = LinkedList()
        a.insert('foo', 0)
        a.insert('bar', 0)
        self.assertEqual(a.size(), 2)


    def test_ll_delete_first_position(self):
        '''
        Test delete function in first position.
        '''
        a = LinkedList()
        a.insert('foo', 0)
        self.assertEqual(a.size(), 1)
        a.delete(0)
        self.assertEqual(a.size(), 0)


    def test_ll_delete_in_non_zero_position(self):
        '''
        Test delete in a non-zero index/position.
        '''
        a = LinkedList()
        a.insert('foo', 0)
        a.insert('bar', 1)
        a.insert('spam', 2)
        a.insert('jazzhands', 3)
        a.delete(2)
        self.assertEqual(a.access_data(0), 'foo')
        self.assertEqual(a.access_data(1), 'bar')
        self.assertEqual(a.access_data(2), 'jazzhands')
        a.delete(1)
        self.assertEqual(a.access_data(0), 'foo')
        self.assertEqual(a.access_data(1), 'jazzhands')

    def test_revser_ll_single_item_ll(self):
        '''
        Test member function if there is only a 
        single node in the ll.
        '''
        a = LinkedList()
        a.insert('foo', 0)
        a.reverse(a.head)
        self.assertEqual(a.access_data(0), 'foo')
        self.assertEqual(a.head.data, 'foo')
        self.assertIsNone(a.head.next_node)


    def test_reverse_ll(self):
        '''
        Test member function that reverses the ll.
        '''
        a = LinkedList()
        a.insert('foo', 0)
        a.insert('bar', 1)
        a.insert('spam', 2)
        a.insert('jazzhands', 3)
        a.reverse(a.head)
        self.assertEqual(a.access_data(0), 'jazzhands')
        self.assertEqual(a.access_data(1), 'spam')
        self.assertEqual(a.access_data(2), 'bar')
        self.assertEqual(a.access_data(3), 'foo')
        self.assertEqual(a.head.data, 'jazzhands')
if __name__ == "__main__":
    unittest.main()

