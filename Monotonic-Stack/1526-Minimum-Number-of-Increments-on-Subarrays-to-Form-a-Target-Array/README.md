> 📌 **Cross-listed:** Primary location is [Array/1526-Minimum-Number-of-Increments-on-Subarrays-to-Form-a-Target-Array](../../Array/1526-Minimum-Number-of-Increments-on-Subarrays-to-Form-a-Target-Array). This problem also appears under: **Array**, **Dynamic Programming**, **Stack**, **Greedy**, **Monotonic Stack**

# 1526. Minimum Number of Increments on Subarrays to Form a Target Array


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/)


## 📝 Problem Description

You are given an integer array `target`. You have an integer array `initial` of the same size as `target` with all elements initially zeros.

In one operation you can choose **any** subarray from `initial` and increment each value by one.

Return *the minimum number of operations to form a *`target`* array from *`initial`.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:**

```

**Input:** target = [1,2,3,2,1]
**Output:** 3
**Explanation:** We need at least 3 operations to form the target array from the initial array.
[**0,0,0,0,0**] increment 1 from index 0 to 4 (inclusive).
[1,**1,1,1**,1] increment 1 from index 1 to 3 (inclusive).
[1,2,**2**,2,1] increment 1 at index 2.
[1,2,3,2,1] target array is formed.

```

Example 2:**

```

**Input:** target = [3,1,1,2]
**Output:** 4
**Explanation:** [**0,0,0,0**] -> [1,1,1,**1**] -> [**1**,1,1,2] -> [**2**,1,1,2] -> [3,1,1,2]

```

Example 3:**

```

**Input:** target = [3,1,5,4,2]
**Output:** 7
**Explanation:** [**0,0,0,0,0**] -> [**1**,1,1,1,1] -> [**2**,1,1,1,1] -> [3,1,**1,1,1**] -> [3,1,**2,2**,2] -> [3,1,**3,3**,2] -> [3,1,**4**,4,2] -> [3,1,5,4,2].

```

 

**Constraints:**

	- `1 <= target.length <= 10^5`

	- `1 <= target[i] <= 10^5`

	- ​​​​​​​The input is generated such that the answer fits inside a 32 bit integer.

## 🧠 Solution Explanation

**Intuition**
The solution takes advantage of the fact that the target array is formed by incrementing subarrays of the initial array. If a subarray is incremented, all elements in that subarray will be equal. Therefore, we can focus on finding the minimum number of increments needed to make each element in the target array equal to the next element.

**Approach**
1. Initialize the result `res` with the first element of the target array.
2. Iterate through the target array starting from the second element.
3. For each element, if it is greater than the previous element, increment the result by the difference between the current element and the previous element.
4. Return the result.

**Time Complexity**
O(n), where n is the length of the target array. This is because we only need to iterate through the target array once to find the minimum number of increments.

**Space Complexity**
O(1), as we only use a constant amount of space to store the result and the previous element.

**Key Insight**
The key insight is that we can focus on making each element in the target array equal to the next element by incrementing subarrays, which allows us to simplify the problem and find a linear-time solution. This insight is crucial in solving this problem efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 43 ms (Beats 64.07%) |
| 💾 Memory | 26.4 MB (Beats 100%) |
| 📅 Solved | 2025-10-30 |
| 💻 Language | Python |