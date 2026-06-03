# 981. Time Based Key-Value Store


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Design](https://img.shields.io/badge/Design-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/time-based-key-value-store/)


## 📝 Problem Description

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:

	- `TimeMap()` Initializes the object of the data structure.

	- `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.

	- `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

 

Example 1:**

```

**Input**
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
**Output**
[null, null, "bar", "bar", null, "bar2", "bar2"]

**Explanation**
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"

```

 

**Constraints:**

	- `1 <= key.length, value.length <= 100`

	- `key` and `value` consist of lowercase English letters and digits.

	- `1 <= timestamp <= 10^7`

	- All the timestamps `timestamp` of `set` are strictly increasing.

	- At most `2 * 10^5` calls will be made to `set` and `get`.

## 🧠 Solution Explanation

**Intuition**
This solution utilizes a hash table to store key-value pairs along with their timestamps. The key insight is to use a binary search approach to efficiently retrieve the value at a given timestamp. The hash table stores lists of tuples, where each tuple contains the value and timestamp.

**Approach**

1. In the `__init__` method, we initialize a hash table `self.h1` with a default value of an empty list.
2. In the `set` method, we append a tuple containing the value and timestamp to the list associated with the given key.
3. In the `get` method, we first retrieve the list of tuples for the given key. If the key is not present, we return an empty string.
4. We perform a binary search on the list of tuples to find the largest timestamp that is less than or equal to the given timestamp.
5. If a valid timestamp is found, we return the associated value. Otherwise, we return an empty string.

**Time Complexity**
The time complexity of the `set` method is O(1) since we are simply appending to a list. The time complexity of the `get` method is O(log n), where n is the number of timestamps stored for the given key. This is because we are performing a binary search on the list of tuples.

**Space Complexity**
The space complexity is O(n), where n is the total number of key-value pairs stored in the hash table. This is because we are storing all the key-value pairs in the hash table.

**Key Insight**
The key insight is to use a binary search approach to efficiently retrieve the value at a given timestamp. This approach allows us to find the largest timestamp that is less than or equal to the given timestamp in O(log n) time, making the solution efficient for large inputs.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 98 ms (Beats 78.44%) |
| 💾 Memory | 75.1 MB (Beats 5.79%) |
| 📅 Solved | 2025-02-27 |
| 💻 Language | Python |