# 146. LRU Cache


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Design](https://img.shields.io/badge/Design-purple) ![Doubly-Linked List](https://img.shields.io/badge/Doubly--Linked%20List-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/lru-cache/)


## 📝 Problem Description

Design a data structure that follows the constraints of a **[Least Recently Used (LRU) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU)**.

Implement the `LRUCache` class:

	- `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.

	- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.

	- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

 

Example 1:**

```

**Input**
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
**Output**
[null, null, null, 1, null, -1, null, -1, 3, 4]

**Explanation**
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

```

 

**Constraints:**

	- `1 <= capacity <= 3000`

	- `0 <= key <= 10^4`

	- `0 <= value <= 10^5`

	- At most `2 * 10^5` calls will be made to `get` and `put`.

## 🧠 Solution Explanation

**Intuition**
The solution uses an `OrderedDict` to implement the LRU cache, where the keys are the cache entries and the values are the corresponding values. The `OrderedDict` maintains the order of access, allowing for efficient eviction of the least recently used entry.

**Approach**
1. Initialize the cache with a capacity `capacity` and an `OrderedDict` `valmap` to store key-value pairs.
2. In the `get` method:
	* Check if the key exists in the cache. If not, return -1.
	* If the key exists, move it to the end of the `OrderedDict` to mark it as recently used.
3. In the `put` method:
	* If the key already exists, update its value and move it to the end of the `OrderedDict`.
	* If the cache is full and the key does not exist, remove the least recently used entry (the first entry in the `OrderedDict`).
	* Add the new key-value pair to the cache.

**Time Complexity**
The time complexity is O(1) for both `get` and `put` methods, as the operations on the `OrderedDict` (insertion, deletion, and moving to the end) take constant time.

**Space Complexity**
The space complexity is O(capacity), as the cache stores at most `capacity` key-value pairs.

**Key Insight**
The key insight is using an `OrderedDict` to maintain the order of access, allowing for efficient eviction of the least recently used entry. This approach enables the `get` and `put` methods to run in O(1) average time complexity, meeting the problem's requirements.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 92 ms (Beats 91.53%) |
| 💾 Memory | 78.1 MB (Beats 30.72%) |
| 📅 Solved | 2025-05-09 |
| 💻 Language | Python |