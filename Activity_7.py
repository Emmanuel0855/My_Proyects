class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Method to reverse the linked list
    def reversar(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # store next node
            current.next = prev  # reverse current node's pointer
            prev = current  # move prev and current one step forward
            current = next_node
        self.head = prev

    # Method to remove duplicates from the linked list
    def eliminar_duplicados(self):
        current = self.head
        seen = set()  # set to store seen values
        prev = None

        while current:
            if current.data in seen:
                # If value is a duplicate, skip the current node
                prev.next = current.next
            else:
                # If value is not a duplicate, add it to the set
                seen.add(current.data)
                prev = current
            current = current.next

    # Utility method to add a node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Utility method to print the list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(3)
ll.append(5)
ll.append(5)
ll.append(7)
ll.append(6)
ll.append(9)
ll.append(6)

print("Original list:")
ll.print_list()

ll.reversar()
print("\nReversed list:")
ll.print_list()

ll.eliminar_duplicados()
print("\nList after removing duplicates:")
ll.print_list()