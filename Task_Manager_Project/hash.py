# hashmap_demo.py

# Step 1: Read the CSV data
stock_prices = []

with open("stock_prices.csv", "r") as f:
    for line in f:
        tokens = line.strip().split(",")   # strip() removes extra newline
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day, price])

# Step 2: Print all stock prices
print("All Stock Prices:")
print(stock_prices)

# Step 3: Print first element
print("\nFirst Entry:")
print(stock_prices[0])

# Step 4: Find stock price on March 9
print("\nStock Price on March 9:")
for element in stock_prices:
    if element[0] == 'march 9':
        print(element[1])

#another way of storing
stock_prices = {}

with open("stock_prices.csv", "r") as f:
    for line in f:
        tokens = line.strip().split(",")   # strip() removes extra newline
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price

print(stock_prices['march 9'])

def get_hash(key):
    hash = 0
    for char in key:
        hash += ord(char)
    return hash % 100

# Call the function and print the result
print(get_hash('march 6'))

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None        


# Only runs when file is executed directly
if __name__ == '__main__':
    t = HashTable()
    t["march 6"] = 310
    t["march 7"] = 420

    # print the entire array (hash table slots)
    print(t.arr)

    # check specific values
    print("Value for 'march 6':", t["march 6"])
    print("Value for 'march 7':", t["march 7"])

del t["march 6"]
print(t.arr) 