class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                print(f"Data '{key}' found in the list.")
                return
            current = current.next
        print(f"Data '{key}' not found in the list.")

# Example usage
if __name__ == "__main__":
    # Create a linked list and add some elements
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(20)
    linked_list.append(78)

    # Search for specific values
    linked_list.search(20)  # Output: Data '20' found in the list.
    linked_list.search(100)  # Output: Data '40' not found in the list.