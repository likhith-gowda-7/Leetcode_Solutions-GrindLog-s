> 📌 **Cross-listed:** Primary location is [Array/1207-Unique-Number-of-Occurrences](../../Array/1207-Unique-Number-of-Occurrences). This problem also appears under: **Array**, **Hash Table**

# 1207. Unique Number of Occurrences


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/unique-number-of-occurrences/)


## 📝 Problem Description

Given an array of integers `arr`, return `true` *if the number of occurrences of each value in the array is **unique** or *`false`* otherwise*.

 

Example 1:**

```

**Input:** arr = [1,2,2,1,1,3]
**Output:** true
**Explanation:** The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
```

Example 2:**

```

**Input:** arr = [1,2]
**Output:** false

```

Example 3:**

```

**Input:** arr = [-3,0,1,-3,1,1,1,-3,10,0]
**Output:** true

```

 

**Constraints:**

	- `1 <= arr.length <= 1000`

	- `-1000 <= arr[i] <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution works by first counting the occurrences of each number in the array and storing them in a hash table. Then, it checks if the number of occurrences for each number is unique by comparing the length of the hash table with the length of a set created from the hash table's values. If they are equal, it means that each number has a unique number of occurrences.

**Approach**
1. Create an empty hash table `h` to store the count of each number in the array.
2. Iterate through the array `arr`. For each number `num`:
   1. Check if `num` is already in the hash table `h`.
   2. If `num` is in `h`, increment its count by 1.
   3. If `num` is not in `h`, add it to `h` with a count of 1.
3. Create a set `s` from the values in the hash table `h`.
4. Return `True` if the length of `h` is equal to the length of `s`, indicating that each number has a unique number of occurrences.

**Time Complexity**
O(n), where n is the length of the array `arr`. This is because we are iterating through the array once to count the occurrences of each number.

**Space Complexity**
O(n), where n is the length of the array `arr`. This is because in the worst case, we might need to store all numbers in the hash table, resulting in a space complexity of O(n).

**Key Insight**
The key insight here is that a set in Python only stores unique elements, so by comparing the length of the hash table with the length of a set created from its values, we can determine if each number has a unique number of occurrences.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.5 MB (Beats 100%) |
| 📅 Solved | 2024-12-09 |
| 💻 Language | Python |