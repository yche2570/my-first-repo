class Node(object):
    def __init__(self, key, val, nxt=None, pre=None):
        self.key = key
        self.val = val
        self.nxt = nxt
        self.pre = pre
    def __repr__(self):
        rsl = [self.key, self.val, self.nxt.val if self.nxt else 'null', self.pre.val if self.pre else 'null']
        return '.'.join(map(str, rsl))
    def __str__(self):
        return self.__repr__()

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node(-1, 'head')
        self.tail = None(-1, 'tail')
        self.head.nxt = self.tail
        self.tail.pre = self.head
        self.cap = capacity
        self.cache = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        print("Get: ", key)
        if key not in self.cache:
            return -1
        node = self.cache[key]
        if node != self.head:
            if node == self.tail:
                self.tail = node.pre
            node.pre.nxt = node.nxt
            if node.nxt:
                node.nxt.pre = node.pre
            if self.head.nxt:
                self.head.nxt.pre = node
            node.pre = None
            node.nxt = self.head.nxt
            self.head = node
        print('Get Head: ', self.head, ' Tail: ', self.tail)
        return node.val

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        print("Put: ", key, value)
        preExist = key in self.cache
        if not preExist:
            newN = Node(key, value)
            self.cache[key] = newN
            if not self.head:
                self.head = self.tail = newN
            else:
                self.head.pre = newN
                newN.nxt = self.head
                self.head = newN
        else:
            node = self.cache[key]
            node.val = value
            self.get(key) #put node to head
        if (not preExist) and len(self.cache) > self.cap:
            tailN = self.tail
            tailKey = tailN.key
            self.tail = tailN.pre
            if tailN == self.head:
                self.head = None
            del self.cache[tailKey]
        print('Put Head: ', self.head, ' Tail: ', self.tail)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)