> 📌 **Cross-listed:** Primary location is [Array/2141-Maximum-Running-Time-of-N-Computers](../../Array/2141-Maximum-Running-Time-of-N-Computers). This problem also appears under: **Array**, **Binary Search**, **Greedy**, **Sorting**

# 2141. Maximum Running Time of N Computers


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-running-time-of-n-computers/)


## 📝 Problem Description

You have `n` computers. You are given the integer `n` and a **0-indexed** integer array `batteries` where the `i^th` battery can **run** a computer for `batteries[i]` minutes. You are interested in running **all** `n` computers **simultaneously** using the given batteries.

Initially, you can insert **at most one battery** into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery **any number of times**. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.

Note that the batteries cannot be recharged.

Return *the **maximum** number of minutes you can run all the *`n`* computers simultaneously.*

 

Example 1:**

![](https://assets.leetcode.com/uploads/2022/01/06/example1-fit.png)
```

**Input:** n = 2, batteries = [3,3,3]
**Output:** 4
**Explanation:** 
Initially, insert battery 0 into the first computer and battery 1 into the second computer.
After two minutes, remove battery 1 from the second computer and insert battery 2 instead. Note that battery 1 can still run for one minute.
At the end of the third minute, battery 0 is drained, and you need to remove it from the first computer and insert battery 1 instead.
By the end of the fourth minute, battery 1 is also drained, and the first computer is no longer running.
We can run the two computers simultaneously for at most 4 minutes, so we return 4.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2022/01/06/example2.png)
```

**Input:** n = 2, batteries = [1,1,1,1]
**Output:** 2
**Explanation:** 
Initially, insert battery 0 into the first computer and battery 2 into the second computer. 
After one minute, battery 0 and battery 2 are drained so you need to remove them and insert battery 1 into the first computer and battery 3 into the second computer. 
After another minute, battery 1 and battery 3 are also drained so the first and second computers are no longer running.
We can run the two computers simultaneously for at most 2 minutes, so we return 2.

```

 

**Constraints:**

	- `1 <= n <= batteries.length <= 10^5`

	- `1 <= batteries[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The problem is asking us to find the maximum time we can run all `n` computers simultaneously using the given batteries. We can use binary search to find the maximum time, as the time complexity is related to the number of batteries. The key insight is that we can insert or remove batteries from computers at any time, so we can assume that the computers are always running at the maximum possible time.

**Approach**
1. Initialize the search range `[l, r]` to `[min(batteries), sum(batteries) // n]`, where `l` is the minimum time a single battery can run and `r` is the maximum time all batteries can run together.
2. Define a helper function `possible(time)` that checks if it's possible to run all `n` computers for `time` minutes. This function iterates over the batteries and subtracts the minimum of each battery's power and `time` from the total power needed.
3. Perform binary search on the search range `[l, r]`. For each `mid` value, check if it's possible to run all `n` computers for `mid` minutes using the `possible(mid)` function.
4. If `possible(mid)` returns `True`, update the search range to `[mid + 1, r]`. Otherwise, update the search range to `[l, mid - 1]`.
5. Repeat step 4 until the search range is empty. The maximum time we can run all `n` computers simultaneously is the final value of `r`.

**Time Complexity**
The time complexity of this solution is O(n log (sum(batteries) // n)), where n is the number of computers and sum(batteries) // n is the maximum time all batteries can run together. This is because we perform binary search on the search range, which takes O(log (sum(batteries) // n)) time, and we iterate over the batteries in the `possible(mid)` function, which takes O(n) time.

**Space Complexity**
The space complexity of this solution is O(1), as we only use a constant amount of space to store the search range and the helper function's variables.

**Key Insight**
The key insight is that we can use binary search to find the maximum time we can run all `n` computers simultaneously, as the time complexity is related to the number of batteries. This allows us to avoid iterating over the batteries in a brute-force manner, which would take O(n^2) time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1403 ms (Beats 5.1%) |
| 💾 Memory | 31.1 MB (Beats 98.23%) |
| 📅 Solved | 2025-12-01 |
| 💻 Language | Python |