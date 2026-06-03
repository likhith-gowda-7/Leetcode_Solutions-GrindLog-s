# 1550. Three Consecutive Odds


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/three-consecutive-odds/)


## 📝 Problem Description

Given an integer array `arr`, return `true` if there are three consecutive odd numbers in the array. Otherwise, return `false`.
 

Example 1:**

```

**Input:** arr = [2,6,4,1]
**Output:** false
**Explanation:** There are no three consecutive odds.

```

Example 2:**

```

**Input:** arr = [1,2,34,3,4,5,7,23,12]
**Output:** true
**Explanation:** [5,7,23] are three consecutive odds.

```

 

**Constraints:**

	- `1 <= arr.length <= 1000`

	- `1 <= arr[i] <= 1000`

## 🧠 Solution Explanation

**Intuition**
This solution works by iterating through the array and keeping track of the number of consecutive odd numbers encountered. As soon as it finds three consecutive odd numbers, it immediately returns `True`. If it finishes iterating through the array without finding three consecutive odd numbers, it returns `False`.

**Approach**
1. Check if the array has less than 3 elements. If so, return `False` immediately because it's impossible to find 3 consecutive odd numbers.
2. Initialize a counter `c` to 0, which will keep track of the number of consecutive odd numbers.
3. Iterate through the array using a for loop.
4. For each element, check if it's odd by using the modulo operator (`arr[i] % 2 == 1`). If it's odd, increment the counter `c`.
5. If the element is even, reset the counter `c` to 0.
6. If the counter `c` reaches 3, return `True` immediately.
7. If the loop finishes without finding three consecutive odd numbers, return `False`.

**Time Complexity**
O(n), where n is the length of the array. This is because we're iterating through the array once.

**Space Complexity**
O(1), which means the space complexity is constant. We're only using a single variable `c` to keep track of the counter, so the space usage doesn't grow with the size of the input array.

**Key Insight**
The key insight here is that we don't need to store the actual consecutive odd numbers; we only need to keep track of the count of consecutive odd numbers. This allows us to solve the problem in linear time and constant space.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-05-11 |
| 💻 Language | Python |