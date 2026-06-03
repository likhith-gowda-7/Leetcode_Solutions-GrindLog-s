> 📌 **Cross-listed:** Primary location is [Array/2221-Find-Triangular-Sum-of-an-Array](../../Array/2221-Find-Triangular-Sum-of-an-Array). This problem also appears under: **Array**, **Math**, **Simulation**, **Combinatorics**, **Number Theory**

# 2221. Find Triangular Sum of an Array


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple) ![Combinatorics](https://img.shields.io/badge/Combinatorics-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-triangular-sum-of-an-array/)


## 📝 Problem Description

You are given a **0-indexed** integer array `nums`, where `nums[i]` is a digit between `0` and `9` (**inclusive**).

The **triangular sum** of `nums` is the value of the only element present in `nums` after the following process terminates:

	- Let `nums` comprise of `n` elements. If `n == 1`, **end** the process. Otherwise, **create** a new **0-indexed** integer array `newNums` of length `n - 1`.

	- For each index `i`, where `0 <= i < n - 1`, **assign** the value of `newNums[i]` as `(nums[i] + nums[i+1]) % 10`, where `%` denotes modulo operator.

	- **Replace** the array `nums` with `newNums`.

	- **Repeat** the entire process starting from step 1.

Return *the triangular sum of* `nums`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2022/02/22/ex1drawio.png)
```

**Input:** nums = [1,2,3,4,5]
**Output:** 8
**Explanation:**
The above diagram depicts the process from which we obtain the triangular sum of the array.
```

Example 2:**

```

**Input:** nums = [5]
**Output:** 5
**Explanation:**
Since there is only one element in nums, the triangular sum is the value of that element itself.
```

 

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `0 <= nums[i] <= 9`

## 🧠 Solution Explanation

**Intuition**
The triangular sum problem involves repeatedly applying a transformation to the input array, where each element is the sum of the two adjacent elements modulo 10. The process terminates when the array has only one element left, which is the triangular sum of the original array.

**Approach**
1. Initialize a variable `n` to store the length of the input array `nums`.
2. Iterate `n-1` times to apply the transformation to the array.
3. In each iteration, create a new array `new_arr` to store the transformed elements.
4. Iterate through the input array, starting from the second element (index 1), and calculate the sum of each element and its previous element modulo 10.
5. Append the calculated value to the `new_arr`.
6. Replace the input array `nums` with the `new_arr`.
7. Repeat steps 3-6 until the array has only one element left.
8. Return the single element in the array as the triangular sum.

**Time Complexity**
O(n * m), where n is the number of iterations and m is the average number of elements in the array after each iteration. Since the array size decreases by 1 in each iteration, the total number of elements processed is n + (n-1) + ... + 1 = n*(n+1)/2. Therefore, the time complexity is O(n^2).

**Space Complexity**
O(n), as we need to store the transformed array in each iteration, which has a maximum size of n.

**Key Insight**
The key insight is that the transformation process reduces the array size by 1 in each iteration, and the resulting array has only one element left, which is the triangular sum of the original array. This insight allows us to simplify the problem and focus on the iterative process of applying the transformation.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1287 ms (Beats 22.79%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-09-30 |
| 💻 Language | Python |