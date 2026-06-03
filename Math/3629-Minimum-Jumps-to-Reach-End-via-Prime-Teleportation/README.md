> 📌 **Cross-listed:** Primary location is [Array/3629-Minimum-Jumps-to-Reach-End-via-Prime-Teleportation](../../Array/3629-Minimum-Jumps-to-Reach-End-via-Prime-Teleportation). This problem also appears under: **Array**, **Hash Table**, **Math**, **Breadth-First Search**, **Number Theory**

# 3629. Minimum Jumps to Reach End via Prime Teleportation


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/)


## 📝 Problem Description

You are given an integer array `nums` of length `n`.

You start at index 0, and your goal is to reach index `n - 1`.

From any index `i`, you may perform one of the following operations:

	- **Adjacent Step**: Jump to index `i + 1` or `i - 1`, if the index is within bounds.

	- **Prime Teleportation**: If `nums[i]` is a prime number `p`, you may instantly jump to any index `j != i` such that `nums[j] % p == 0`.

Return the **minimum** number of jumps required to reach index `n - 1`.

 

Example 1:**

**Input:** nums = [1,2,4,6]

**Output:** 2

**Explanation:**

One optimal sequence of jumps is:

	- Start at index `i = 0`. Take an adjacent step to index 1.

	- At index `i = 1`, `nums[1] = 2` is a prime number. Therefore, we teleport to index `i = 3` as `nums[3] = 6` is divisible by 2.

Thus, the answer is 2.

Example 2:**

**Input:** nums = [2,3,4,7,9]

**Output:** 2

**Explanation:**

One optimal sequence of jumps is:

	- Start at index `i = 0`. Take an adjacent step to index `i = 1`.

	- At index `i = 1`, `nums[1] = 3` is a prime number. Therefore, we teleport to index `i = 4` since `nums[4] = 9` is divisible by 3.

Thus, the answer is 2.

Example 3:**

**Input:** nums = [4,6,5,8]

**Output:** 3

**Explanation:**

	- Since no teleportation is possible, we move through `0 &rarr; 1 &rarr; 2 &rarr; 3`. Thus, the answer is 3.

 

**Constraints:**

	- `1 <= n == nums.length <= 10^5`

	- `1 <= nums[i] <= 10^6`

## 🧠 Solution Explanation

**Intuition**
This solution uses a combination of dynamic programming and a prime number sieve to efficiently find the minimum number of jumps required to reach the end of the array. The key insight is to use a hash table to store the indices of numbers that can be reached by prime teleportation, allowing for fast lookup and update of the dynamic programming table.

**Approach**
1. Create a prime number sieve to generate a list of prime numbers up to a certain limit.
2. Initialize a hash table `head` to store the indices of numbers that can be reached by prime teleportation.
3. Initialize a dynamic programming table `dp` to store the minimum number of jumps required to reach each index.
4. Initialize a queue with the starting index (0) and a set to keep track of seen prime numbers.
5. While the queue is not empty, pop an index from the queue and update the dynamic programming table and the queue with its adjacent indices and prime teleportation indices.
6. If the end index is reached, return the minimum number of jumps required.

**Time Complexity**
O(n + m log log m), where n is the length of the array and m is the maximum value in the array. The prime number sieve takes O(m log log m) time, and the dynamic programming and queue operations take O(n) time.

**Space Complexity**
O(m + n), where m is the maximum value in the array and n is the length of the array. The prime number sieve and hash table take O(m) space, and the dynamic programming table and queue take O(n) space.

**Key Insight**
The key insight is to use a hash table to store the indices of numbers that can be reached by prime teleportation, allowing for fast lookup and update of the dynamic programming table. This allows the solution to efficiently handle the prime teleportation operation and find the minimum number of jumps required to reach the end of the array.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 476 ms (Beats 98.01%) |
| 💾 Memory | 51.5 MB (Beats 81.6%) |
| 📅 Solved | 2026-05-08 |
| 💻 Language | Python |