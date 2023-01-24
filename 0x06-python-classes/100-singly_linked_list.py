#!/usr/bin/python3
"""
A class representing a node in a singly linked list
"""


class Node:
    """
    A class representing a node in a singly linked list
    """
    def __init__(self, data, next_node=None):
        """
        Initialize a new Node object with given data and next_node.
        :param data: an integer representing the data of the node
        :param next_node: a Node object representing the next node
        in the linked list. Default is None.
        :raises TypeError: if data is not an integer
        :raises TypeError: if next_node is not None and not a Node object
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self._data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data of the node
        :return: an integer representing the data of the node
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Set the data of the node
        :param value: an integer representing the new data of the node
        :raises TypeError: if value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Get the next node of the linked list
        :return: a Node object representing the next node in the linked list.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node of the linked list
        :param value: a Node object representing the next node
        in the linked list.
        :raises TypeError: if value is not None and not a Node object
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


"""
A class representing a singly linked list
"""


class SinglyLinkedList:
    """
    A class representing a singly linked list
    """
    def __init__(self):
        """
        Initialize a new SinglyLinkedList object.
        """
        self.head = None

    def __str__(self):
        """
        Get a string representation of the linked list,
        with each node's data on a new line.
        :return: a string representation of the linked list
        """
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Insert a new node with given value into the correct sorted
        position in the linked list (increasing order)
        :param value: an integer representing the data of the new node
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node
