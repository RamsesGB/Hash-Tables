# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.key}, {self.value}, {self.next}"


class LinkedList:
    def __init__(self, head=None, next_node=None):
        self.head = head
        self.next = next_node

    def add_to_head(self, node):
        if self.head is None:
            self.head = node

        node.next = self.head
        self.head = node

    def find_key(self, key):
        current = self.head

        while current is not None:
            if current.key == key:
                return current.value
            else:
                current = current.next

        return None

    def remove(self, key):
        if self.head.key == key:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:
            if current.next.key == key:
                current.next = current.next.next
            else:
                current = current.next

        return None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        hashed = 0
        prime = 31
        for char in key:
            hashed = prime * hashed + ord(char)
        return hashed

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        index = self._hash_mod(key)
        print(index)

        new_pair = LinkedPair(key, value)
        new_linked_list = LinkedList(new_pair)

        if self.storage[index] is None:
            self.storage[index] = new_linked_list
        else:
            self.storage[index].add_to_head(new_pair)

    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is None:
            return None
        else:
            self.storage[index].remove(key)

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is None:
            return None
        else:
            return self.storage[index].find_key(key)

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        self.capacity *= 2

        new_storage = [None] * self.capacity

        old = self.storage[:]

        self.storage = new_storage

        for i in range(len(old)):
            if old[i] is not None:
                current = old[i].head

                while current is not None:
                    self.insert(current.key, current.value)
                    current = current.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

    ht.remove("line_1")
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
