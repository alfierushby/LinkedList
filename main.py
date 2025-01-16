class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value) if self.next is None else str(self.value) + " -> " + str(self.next)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__length = 0

    def add_node(self, value):
        if type(value) is not float and type(value) is not int:
            raise TypeError('Value can only be a number')
        self.__length += 1
        new_node = Node(value, None)
        if self.head is None:
            self.head = new_node
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node

    def print_nodes(self):
        print(self.head)

    def delete_node_match(self, value):
        self.__delete_node_match_recursive(value, self.head)

    def __delete_node_match_recursive(self, value, node):
        if node is None or node.next is None:
            return

        if node.next.value == value:
            self.__length -= 1
            node.next = node.next.next
            return

        self.__delete_node_match_recursive(value, node.next)

    def delete_node_index(self, index):
        current_node = self.head
        if index < 0:
            return

        for i in range(index - 1):
            current_node = current_node.next
            if current_node is None:
                return

        self.__length -= 1
        current_node.next = current_node.next.next

    def sort(self):
        for i in range(self.__length):
            self.__bubble_pass(self.head)

    def __bubble_pass(self, node):
        if node.next is None:
            return
        if node.value <= node.next.value:
            self.__bubble_pass(node.next)
        else:
            # Swap otherwise
            temp = node.value
            node.value = node.next.value
            node.next.value = temp
            self.__bubble_pass(node.next)

    def insert_sorted(self, value):
        if type(value) is not float and type(value) is not int:
            raise TypeError('Value can only be a number')

        current_node = self.head

        while current_node.next.value <= value:
            current_node = current_node.next

        current_node.next = Node(value, current_node.next)

    def reverse_list(self):
        old_head = self.head

        current_node = self.head
        prev_node = None

        while current_node is not None:
            temp = current_node.next
            # Make the current node point to the previous node
            current_node.next = prev_node

            prev_node = current_node
            current_node = temp

        self.head = self.tail
        self.tail = old_head


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add_node(1)
    linked_list.add_node(14)
    linked_list.add_node(2)
    linked_list.add_node(3)
    linked_list.add_node(6)
    linked_list.print_nodes()
    linked_list.sort()
    linked_list.print_nodes()
    linked_list.insert_sorted(8)
    linked_list.print_nodes()
    linked_list.reverse_list()
    linked_list.print_nodes()
    linked_list.add_node(5)
    linked_list.print_nodes()
    linked_list.sort()
    linked_list.print_nodes()
