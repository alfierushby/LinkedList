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

    def add_node(self, value):
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
            node.next = node.next.next
            return

        self.__delete_node_match_recursive(value, node.next)

    def delete_node_index(self, index):
        current_node = self.head
        if index == 0:
            self.head = current_node.next
            return
        if index < 0:
            return

        for i in range(index - 1):
            current_node = current_node.next
            if current_node is None:
                return

        current_node.next = current_node.next.next

    def sort(self):
        current_node = self.head
        while current_node is not None:
            self.__bubble_pass(current_node)
            current_node = current_node.next

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
        current_node = self.head

        while current_node.next.value <= value:
            current_node = current_node.next

        current_node.next = Node(value, current_node.next)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

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
