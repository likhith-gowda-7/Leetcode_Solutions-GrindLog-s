> 📌 **Cross-listed:** Primary location is [Array/0416-Partition-Equal-Subset-Sum](../../Array/0416-Partition-Equal-Subset-Sum). This problem also appears under: **Array**, **Dynamic Programming**

# 416. Partition Equal Subset Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/)


## 📝 Problem Description

Given an integer array `nums`, return `true` *if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or *`false`* otherwise*.

 

Example 1:**

```

**Input:** nums = [1,5,11,5]
**Output:** true
**Explanation:** The array can be partitioned as [1, 5, 5] and [11].

```

Example 2:**

```

**Input:** nums = [1,2,3,5]
**Output:** false
**Explanation:** The array cannot be partitioned into equal sum subsets.

```

 

**Constraints:**

	- `1 <= nums.length <= 200`

	- `1 <= nums[i] <= 100`

## 🧠 Solution Explanation

### Intuition
This solution works by attempting to find a subset of the input array that sums up to half of the total sum of the array. If such a subset exists, it means the array can be partitioned into two subsets with equal sums. The approach uses dynamic programming to efficiently explore all possible subsets.

### Approach
1. Calculate the total sum of the input array and check if it's odd. If it's odd, return False because it's impossible to partition the array into two subsets with equal sums.
2. Initialize a set `dp` to store the sums of subsets found so far, starting with 0.
3. Iterate through each number in the input array. For each number, create a copy of the current `dp` set and iterate through each sum in the copy.
4. For each sum, calculate the new sum by adding the current number. If the new sum equals the target sum (half of the total sum), return True.
5. Add the new sum to the copy of the `dp` set.
6. After iterating through all numbers, update the `dp` set with the copy.

### Time Complexity
The time complexity is O(n * sum), where n is the length of the input array and sum is the total sum of the array. This is because in the worst case, we iterate through each number in the array and for each number, we iterate through each sum in the `dp` set.

### Space Complexity
The space complexity is O(sum), where sum is the total sum of the array. This is because we store the sums of subsets in the `dp` set, which can grow up to the total sum of the array.

### Key Insight
The key insight is to use a set to store the sums of subsets found so far, which allows us to efficiently explore all possible subsets and avoid duplicates. This approach enables us to solve the problem in a reasonable time complexity despite the large search space.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 147 ms (Beats 97.93%) |
| 💾 Memory | 19 MB (Beats 99.76%) |
| 📅 Solved | 2025-11-29 |
| 💻 Language | Python |