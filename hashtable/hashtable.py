hash_table = [[] for _ in range (10)]
# print(hash_table)

#function to insert values in hash table
def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i,kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))

insert(hash_table,10,'Apple')
insert(hash_table,23,'Android')
insert(hash_table,21,'Windows')
# print(hash_table)

#function to search a value from hash table
def search(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return v

# print(search(hash_table, 10))
# print(search(hash_table, 23))
# print(search(hash_table, 21))

# delete data from hash table
def delete(hash_table, key):
    hash_key = hash(key) % len(hash_table)    
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv 
        if key == k:
            key_exists = True 
            break
    if key_exists:
        del bucket[i]
        print ('Key {} deleted'.format(key))
    else:
        print ('Key {} not found'.format(key))

print(hash_table)
print('Deleting value with key 100')
delete(hash_table, 100)
print('Deleting value with key 10')
delete(hash_table, 10)
print(hash_table)