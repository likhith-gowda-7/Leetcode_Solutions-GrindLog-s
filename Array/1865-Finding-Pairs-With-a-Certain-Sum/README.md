# 1865. Finding Pairs With a Certain Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Design](https://img.shields.io/badge/Design-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/finding-pairs-with-a-certain-sum/)


## 📝 Problem Description

You are given two integer arrays `nums1` and `nums2`. You are tasked to implement a data structure that supports queries of two types:

	- **Add** a positive integer to an element of a given index in the array `nums2`.

	- **Count** the number of pairs `(i, j)` such that `nums1[i] + nums2[j]` equals a given value (`0 <= i < nums1.length` and `0 <= j < nums2.length`).

Implement the `FindSumPairs` class:

	- `FindSumPairs(int[] nums1, int[] nums2)` Initializes the `FindSumPairs` object with two integer arrays `nums1` and `nums2`.

	- `void add(int index, int val)` Adds `val` to `nums2[index]`, i.e., apply `nums2[index] += val`.

	- `int count(int tot)` Returns the number of pairs `(i, j)` such that `nums1[i] + nums2[j] == tot`.

 

Example 1:**

```

**Input**
["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
**Output**
[null, 8, null, 2, 1, null, null, 11]

**Explanation**
FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
findSumPairs.count(7);  // return 8; pairs (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) make 2 + 5 and pairs (5,1), (5,5) make 3 + 4
findSumPairs.add(3, 2); // now nums2 = [1,4,5,**4**`,5,4`]
findSumPairs.count(8);  // return 2; pairs (5,2), (5,4) make 3 + 5
findSumPairs.count(4);  // return 1; pair (5,0) makes 3 + 1
findSumPairs.add(0, 1); // now nums2 = [**`2`**,4,5,4`,5,4`]
findSumPairs.add(1, 1); // now nums2 = [`2`,**5**,5,4`,5,4`]
findSumPairs.count(7);  // return 11; pairs (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) make 2 + 5 and pairs (5,3), (5,5) make 3 + 4

```

 

**Constraints:**

	- `1 <= nums1.length <= 1000`

	- `1 <= nums2.length <= 10^5`

	- `1 <= nums1[i] <= 10^9`

	- `1 <= nums2[i] <= 10^5`

	- `0 <= index < nums2.length`

	- `1 <= val <= 10^5`

	- `1 <= tot <= 10^9`

	- At most `1000` calls are made to `add` and `count` **each**.

## 🧠 Solution Explanation

**Intuition**
The solution utilizes a combination of a hash map and a list to efficiently store and update the elements of `nums2`. By maintaining a count of each element in `nums2` using a hash map, we can quickly determine the number of pairs that sum up to a given value. The list is used to update the value at a specific index in `nums2`.

**Approach**
1. In the constructor, initialize two hash maps `h1` and `h2` to store the frequency of elements in `nums1` and `nums2`, respectively. Also, store the original `nums2` list in `self.nums2`.
2. In the `add` method, update the value at the specified index in `nums2` by adding the given value `val`. Decrement the count of the old value in `h2` and increment the count of the new value.
3. In the `count` method, iterate through the elements of `nums1` and for each element, check if its complement (i.e., the value we need to get by adding it to `nums2[j]`) exists in `h2`. If it does, multiply the frequency of the complement in `h2` by the frequency of the current element in `h1` and add the result to the total count of pairs.

**Time Complexity**
- `add` method: O(1) because hash map operations (decrement, increment) take constant time.
- `count` method: O(n) where n is the number of unique elements in `nums1`, because we iterate through all elements in `nums1` and perform a hash map lookup for each element.

**Space Complexity**
- The space complexity is O(n) where n is the number of unique elements in `nums2`, because we store the frequency of each element in `h2`.

**Key Insight**
The key insight is to maintain a count of each element in `nums2` using a hash map, which allows us to quickly determine the number of pairs that sum up to a given value. This approach enables us to efficiently handle the `count` method, which would be O(n^2) if we had to iterate through all elements in `nums2` for each element in `nums1`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 173 ms (Beats 79.75%) |
| 💾 Memory | 48.3 MB (Beats 85.36%) |
| 📅 Solved | 2025-07-06 |
| 💻 Language | Python |