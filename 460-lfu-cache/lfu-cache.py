class LFUCache:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.freq = 1
            self.prev = None
            self.next = None

    class DLL:
        def __init__(self):
            self.head = LFUCache.Node(-1, -1)
            self.tail = LFUCache.Node(-1, -1)

            self.head.next = self.tail
            self.tail.prev = self.head

            self.size = 0

        def add(self, node):
            # Add at the end = most recently used
            node.prev = self.tail.prev
            node.next = self.tail

            self.tail.prev.next = node
            self.tail.prev = node

            self.size += 1

        def remove(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev

            self.size -= 1

        def remove_first(self):
            if self.size == 0:
                return None

            node = self.head.next
            self.remove(node)

            return node


    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0

        # key -> Node
        self.cache = {}

        # frequency -> DLL
        self.freq_map = {}

        # Minimum frequency currently present
        self.min_freq = 0


    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.update_frequency(node)

        return node.value


    def put(self, key, value):

        if self.capacity == 0:
            return

        # Key already exists
        if key in self.cache:

            node = self.cache[key]
            node.value = value

            self.update_frequency(node)

            return

        # Cache is full
        if self.size == self.capacity:

            # Get LFU list
            lfu_list = self.freq_map[self.min_freq]

            # Remove LRU from LFU list
            node = lfu_list.remove_first()

            del self.cache[node.key]

            self.size -= 1

        # Create new node
        node = self.Node(key, value)

        self.cache[key] = node

        # New node always has frequency 1
        if 1 not in self.freq_map:
            self.freq_map[1] = self.DLL()

        self.freq_map[1].add(node)

        self.min_freq = 1

        self.size += 1


    def update_frequency(self, node):

        old_freq = node.freq

        old_list = self.freq_map[old_freq]

        # Remove from old frequency list
        old_list.remove(node)

        # If this was the minimum frequency
        if old_freq == self.min_freq and old_list.size == 0:
            self.min_freq += 1

        # Increase frequency
        node.freq += 1

        new_freq = node.freq

        # Create list if needed
        if new_freq not in self.freq_map:
            self.freq_map[new_freq] = self.DLL()

        # Add to new frequency list
        self.freq_map[new_freq].add(node)