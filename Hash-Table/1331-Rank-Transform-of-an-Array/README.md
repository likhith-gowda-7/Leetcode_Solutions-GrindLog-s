> 📌 **Cross-listed:** Primary location is [Array/1331-Rank-Transform-of-an-Array](../../Array/1331-Rank-Transform-of-an-Array). This problem also appears under: **Array**, **Hash Table**, **Sorting**

# 1331. Rank Transform of an Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-JavaScript-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/rank-transform-of-an-array/)


## 📝 Problem Description

Given an array of integers `arr`, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

	- Rank is an integer starting from 1.

	- The larger the element, the larger the rank. If two elements are equal, their rank must be the same.

	- Rank should be as small as possible.

 

Example 1:**

```

**Input:** arr = [40,10,20,30]
**Output:** [4,1,2,3]
**Explanation**: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
```

Example 2:**

```

**Input:** arr = [100,100,100]
**Output:** [1,1,1]
**Explanation**: Same elements share the same rank.

```

Example 3:**

```

**Input:** arr = [37,12,28,9,100,56,80,5,12]
**Output:** [5,3,4,2,8,6,7,1,3]

```

 

**Constraints:**

	- `0 <= arr.length <= 10^5`

	- `-10^9 <= arr[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution works by first creating a sorted array of unique elements from the input array. Then, it creates a hash table that maps each element to its rank. Finally, it uses the map function to replace each element in the input array with its corresponding rank.

**Approach**
1. Check if the input array is empty and return an empty array if it is.
2. Create a sorted array of unique elements from the input array by converting it to a set and then sorting the set.
3. Create a hash table that maps each element to its rank by iterating over the sorted array and assigning each element a rank based on its index.
4. Use the map function to replace each element in the input array with its corresponding rank in the hash table.

**Time Complexity**
O(n log n) due to the sorting operation, where n is the number of unique elements in the input array.

**Space Complexity**
O(n) for storing the sorted array of unique elements and the hash table.

**Key Insight**
The key insight is to first create a sorted array of unique elements, which allows us to easily assign ranks to each element. This approach takes advantage of the fact that the rank of an element is determined by its value, and the sorted array provides a convenient way to map values to ranks.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 188 ms (Beats 6.56%) |
| 💾 Memory | 83.2 MB (Beats 32.24%) |
| 📅 Solved | 2024-10-04 |
| 💻 Language | JavaScript |