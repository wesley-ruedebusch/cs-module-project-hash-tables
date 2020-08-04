from linked_list import LinkedList


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [LinkedList()] * capacity
        self.load = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        return self.load / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """
        hash = 14695981039346656037

        byteKey = key.encode()
        for b in byteKey:
            hash *= 1099511628211
            hash ^= b
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = ((hash << 5) + hash) + ord(c)
            hash &= 0xffffffff
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        index = self.hash_index(key)
        slot = self.data[index]
        element = slot.head

        # handle overwrites
        while element is not None:
            if element.key == key:
                element.value = value
                return
            element = element.next

        newElement = HashTableEntry(key, value)
        slot.insert_at_head(newElement)
        self.load += 1

        if self.get_load_factor() > 0.7:
            self.resize(2 * self.capacity)

        # if self.data[index] is None:  # empty slot in the array
        #     self.data[index] = HashTableEntry(key, value)
        #     self.load += 1
        # else:
        #     node = self.data[index]
        #     if node.key == key:  # handles overwrites
        #         node.value = value
        #     else:  # else, insert new node at the head
        #         newNode = HashTableEntry(key, value)
        #         newNode.next = self.head
        #         self.head = newNode
        #         self.load += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # self.put(key, None)
        # self.load -= 1

        index = self.hash_index(key)
        slot = self.data[index]
        element = slot.head
        
        while element is not None:
            if element.key == key:
               slot.delete(element.value)
               self.load -= 1
               if self.get_load_factor() < 0.2:
                    self.resize(int(0.5 * self.capacity))
               return
            element = element.next
        print("Warning: The key was not found.")

        # index = self.hash_index(key)
        # if self.data[index] == None:
        #     print("Warning: The key was not found.")
        # else:
        #     self.data[index] = None
        #     self.load -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        slot = self.data[index]
        element = slot.head
        while element:
            if element.key == key:
                return element.value
            element = element.next
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        if new_capacity < MIN_CAPACITY:
            resize_capacity = MIN_CAPACITY
        else:
            resize_capacity = new_capacity

        data_copy = self.data
        self.data = [LinkedList()] * resize_capacity
        self.load = 0
        self.capacity = resize_capacity
        for item in data_copy:
            element = item.head
            while element is not None:
                self.put(element.key, element.value)
                element = element.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
