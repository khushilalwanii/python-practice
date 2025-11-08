# Implement hash table collision handling using linear probing

class HashTable:  
    def __init__(self):
        # Keeping size small to demonstrate linear probing easily
        self.MAX = 10
        self.arr = [None for _ in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def get_prob_range(self, index):
        # Returns list of indices to probe in circular manner
        return [*range(index, len(self.arr))] + [*range(0, index)]
    
    def find_slot(self, key, index):
        # Finds the next available slot or the slot with the same key
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap full")

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, val)
        print(self.arr)

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return None
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return None
            if element[0] == key:
                return element[1]
        return None

    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return  # item not found
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None
                break
        print(self.arr)


# ------------------------------
# Example usage:
# ------------------------------
if __name__ == "__main__":
    t = HashTable()
    t["march 6"] = 20
    t["march 17"] = 88
    t["march 17"] = 29
    t["nov 1"] = 1
    t["march 33"] = 234
    print("Value for 'march 33':", t["march 33"])
    t["march 33"] = 999
    print("Updated 'march 33':", t["march 33"])
    t["april 1"] = 87
    t["april 2"] = 123
    t["april 3"] = 234234
    t["april 4"] = 91
    t["May 22"] = 4
    t["May 7"] = 47

    # Try deleting and reinserting
    del t["april 2"]
    t["Jan 1"] = 0

    print("\nFinal Hash Table:")
    print(t.arr)
