> 📌 **Cross-listed:** Primary location is [Hash Table/0460-LFU-Cache](../../Hash-Table/0460-LFU-Cache). This problem also appears under: **Hash Table**, **Linked List**, **Design**, **Doubly-Linked List**

# 460. LFU Cache


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Design](https://img.shields.io/badge/Design-purple) ![Doubly-Linked List](https://img.shields.io/badge/Doubly--Linked%20List-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/lfu-cache/)


## 📝 Problem Description

Design and implement a data structure for a [Least Frequently Used (LFU)](https://en.wikipedia.org/wiki/Least_frequently_used) cache.

Implement the `LFUCache` class:

	- `LFUCache(int capacity)` Initializes the object with the `capacity` of the data structure.

	- `int get(int key)` Gets the value of the `key` if the `key` exists in the cache. Otherwise, returns `-1`.

	- `void put(int key, int value)` Update the value of the `key` if present, or inserts the `key` if not already present. When the cache reaches its `capacity`, it should invalidate and remove the **least frequently used** key before inserting a new item. For this problem, when there is a **tie** (i.e., two or more keys with the same frequency), the **least recently used** `key` would be invalidated.

To determine the least frequently used key, a **use counter** is maintained for each key in the cache. The key with the smallest **use counter** is the least frequently used key.

When a key is first inserted into the cache, its **use counter** is set to `1` (due to the `put` operation). The **use counter** for a key in the cache is incremented either a `get` or `put` operation is called on it.

The functions get` and put` must each run in `O(1)` average time complexity.

 

Example 1:**

```

**Input**
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
**Output**
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

**Explanation**
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3

```

 

**Constraints:**

	- `1 <= capacity <= 10^4`

	- `0 <= key <= 10^5`

	- `0 <= value <= 10^9`

	- At most `2 * 10^5` calls will be made to `get` and `put`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a combination of two hash maps and an ordered dictionary to efficiently manage the LFU cache. The first hash map (`cntmap`) stores the frequency count of each key, while the second hash map (`freqmap`) stores the elements for each frequency count. The ordered dictionary ensures that the least frequently used key is always removed first.

**Approach**
1. Initialize the `cntmap` and `freqmap` hash maps in the `__init__` method.
2. In the `Counter` method:
	* Increment the frequency count of the given key in `cntmap`.
	* Remove the key from the ordered dictionary in `freqmap` with the old frequency count.
	* If the ordered dictionary is empty for the old frequency count, remove it from `freqmap`.
	* Increment the least frequency count (`lfucnt`) if necessary.
	* Add the key to the new frequency count's ordered dictionary in `freqmap`.
3. In the `get` method:
	* Check if the key exists in `cntmap`. If not, return -1.
	* Call the `Counter` method to update the frequency count and return the value.
4. In the `put` method:
	* If the key already exists, update its value in `freqmap` and call `Counter` to update the frequency count.
	* If the key does not exist and the cache is full, remove the least frequently used key from `freqmap` and `cntmap`.
	* Add the new key to `cntmap` and `freqmap` with a frequency count of 1.

**Time Complexity**
- `get` and `put` operations: O(1) amortized, because the `Counter` method is called in `get` and `put`, which updates the frequency count and removes the least frequently used key if necessary.
- `put` operation when the cache is full: O(1) because we only need to remove the least frequently used key from `freqmap` and `cntmap`.

**Space Complexity**
- O(n) for the `cntmap` and `freqmap` hash maps, where n is the number of keys in the cache.

**Key Insight**
The key insight is to use a combination of two hash maps and an ordered dictionary to efficiently manage the LFU cache. By storing the frequency count of each key and the elements for each frequency count, we can quickly update the frequency count and remove the least frequently used key when the cache is full.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 127 ms (Beats 78.51%) |
| 💾 Memory | 79.9 MB (Beats 6.47%) |
| 📅 Solved | 2025-05-09 |
| 💻 Language | Python |