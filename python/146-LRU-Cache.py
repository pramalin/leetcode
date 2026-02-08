class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = []  # To keep track of the order of keys for LRU eviction

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed key to the end (most recently used)
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing key
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            # Remove the least recently used key
            lru_key = self.order.pop(0)
            del self.cache[lru_key]
        
        # Add or update the key-value pair
        self.cache[key] = value
        self.order.append(key)


# Your LRUCache object will be instantiated and called as such:
#obj = LRUCache(capacity)
#obj.put(key,value)
#param_1 = obj.get(key)

opsInput = ["LRUCache","put","put","get","put","get","put","get","get","get"]
valuesInput = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
expected = [None,None,None,1,None,-1,None,-1,3,4]

for op, val, exp in zip(opsInput, valuesInput, expected):
    if op == "LRUCache":
        obj = LRUCache(*val)
        print(f"{op}({val}) -> {exp}")
    elif op == "put":
        obj.put(*val)
        print(f"{op}({val}) -> {exp}")
    elif op == "get":
        result = obj.get(*val)
        passed = result == exp
        print(f"{op}({val}) -> {result} (Expected: {exp}) pass: {passed})")