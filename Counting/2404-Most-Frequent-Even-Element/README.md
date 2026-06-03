> 📌 **Cross-listed:** Primary location is [Array/2404-Most-Frequent-Even-Element](../../Array/2404-Most-Frequent-Even-Element). This problem also appears under: **Array**, **Hash Table**, **Counting**

# 2404. Most Frequent Even Element


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/most-frequent-even-element/)


## 📝 Problem Description

Given an integer array `nums`, return *the most frequent even element*.

If there is a tie, return the **smallest** one. If there is no such element, return `-1`.

 

Example 1:**

```

**Input:** nums = [0,1,2,2,4,4,1]
**Output:** 2
**Explanation:**
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
```

Example 2:**

```

**Input:** nums = [4,4,4,9,2,4]
**Output:** 4
**Explanation:** 4 is the even element appears the most.

```

Example 3:**

```

**Input:** nums = [29,47,21,41,13,37,25,7]
**Output:** -1
**Explanation:** There is no even element.

```

 

**Constraints:**

	- `1 <= nums.length <= 2000`

	- `0 <= nums[i] <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution uses a hash table to count the frequency of each even element in the array. It then iterates through the hash table to find the smallest even element with the maximum frequency.

**Approach**
1. Create a hash table `c` to store the frequency of each element.
2. Iterate through the input array `nums`. For each element `n`, check if it's even by using the modulo operator (`n % 2 == 0`). If it's even, increment its count in the hash table `c`.
3. Check if the hash table `c` is not empty. If it's not empty, find the maximum frequency `h` by getting the maximum value from the hash table.
4. Initialize a variable `ans` to infinity. Iterate through the hash table `c` to find the smallest even element with the maximum frequency `h`. If an element's frequency is equal to `h` and its value is smaller than `ans`, update `ans` with its value.
5. Return `ans` if it's not infinity (i.e., an even element with the maximum frequency was found), otherwise return -1.

**Time Complexity**
O(n), where n is the length of the input array `nums`. This is because we iterate through the array once to count the frequency of each element, and then iterate through the hash table once to find the smallest even element with the maximum frequency.

**Space Complexity**
O(n), where n is the length of the input array `nums`. This is because in the worst case, we might need to store all elements in the hash table.

**Key Insight**
The key insight is to use a hash table to efficiently count the frequency of each element, and then iterate through the hash table to find the smallest even element with the maximum frequency. This approach allows us to solve the problem in linear time and space complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 19 ms (Beats 69.07%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2025-01-14 |
| 💻 Language | Python |