import config

class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    __instance = None

    @staticmethod 
    def getInstance():
      if LRUCache.__instance == None:
          LRUCache()
      return LRUCache.__instance

    def __init__(self):
      print("here2")
      if LRUCache.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         if config.CACHE_SIZE < 1:
            print('LRUCache capacity must be > 0')
            return None

         print("here")
         self.capacity = config.CACHE_SIZE
         self.size = 0 
         self.node_map = {}
         self.head = None
         self.tail = None

         LRUCache.__instance = self

    def __init__(self):
        if config.CACHE_SIZE < 1:
            print('LRUCache capacity must be > 0')
            return None

        self.capacity = config.CACHE_SIZE
        self.size = 0
        self.node_map = {}
        self.head = None
        self.tail = None


    def use_node(self, node):
        if node is self.head:
            return
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        if node is self.tail:
            self.tail = self.tail.prev
        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node

    def get(self, key):
        if key in self.node_map:
            print("here",self.node_map[key] ,self.node_map[key].val)
            self.use_node(self.node_map[key])
            return self.node_map[key].val
        else:
            return -1

    def put(self, key, value):
        if key in self.node_map:
            self.use_node(self.node_map[key])
            self.node_map[key].val = value
        else:
            node = Node(key, value)
            self.node_map[key] = node

            if self.size == 0:
                self.head = node
                self.tail = node

            if self.size < self.capacity:
                self.size += 1

            elif self.size == self.capacity:
                k = self.tail.key

                if self.size == 1:
                    self.head = node
                    self.tail = node
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None

                del self.node_map[k]

            self.use_node(node)
        print(self.node_map)
        print(self.head.val)
        print(self.tail.val)
        return True

    def delete(self, key):
        print(key, self.head.val , self.tail.val)
        try:
            if key not in self.node_map:
                print("key not in key map")
                return False
            else:
                print("here")
                node = self.node_map[key]
                print(node)
                if node == self.head:
                    print("here1")
                    if node.next == None:
                        print("here2")
                        self.head = None
                        self.tail = None
                    else:
                        print("here3")
                        node.next.prev = None
                        self.head = node.next
                        node.next = None
                elif node == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    node.next = None
                    node.prev = None

                del self.node_map[key]
                self.size -= 1

            print(self.node_map)
            return True
        except  Exception as e:
            print("exception raised in delete data", e)

    def fetchall(self):
        all_data = {}
        for i in self.node_map:
            all_data[i] = self.node_map[i].val

        return all_data







