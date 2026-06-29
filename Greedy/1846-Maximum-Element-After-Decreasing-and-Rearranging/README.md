> 📌 **Cross-listed:** Primary location is [Array/1846-Maximum-Element-After-Decreasing-and-Rearranging](../../Array/1846-Maximum-Element-After-Decreasing-and-Rearranging). This problem also appears under: **Array**, **Greedy**, **Sorting**

# 1846. Maximum Element After Decreasing and Rearranging


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/)


## 📝 Problem Description

You are given an array of positive integers `arr`. Perform some operations (possibly none) on `arr` so that it satisfies these conditions:

	- The value of the **first** element in `arr` must be `1`.

	- The absolute difference between any 2 adjacent elements must be **less than or equal to **`1`. In other words, `abs(arr[i] - arr[i - 1]) <= 1` for each `i` where `1 <= i < arr.length` (**0-indexed**). `abs(x)` is the absolute value of `x`.

There are 2 types of operations that you can perform any number of times:

	- **Decrease** the value of any element of `arr` to a **smaller positive integer**.

	- **Rearrange** the elements of `arr` to be in any order.

Return *the **maximum** possible value of an element in *`arr`* after performing the operations to satisfy the conditions*.

 

Example 1:**

```

**Input:** arr = [2,2,1,2,1]
**Output:** 2
**Explanation:** 
We can satisfy the conditions by rearranging `arr` so it becomes `[1,2,2,2,1]`.
The largest element in `arr` is 2.

```

Example 2:**

```

**Input:** arr = [100,1,1000]
**Output:** 3
**Explanation:** 
One possible way to satisfy the conditions is by doing the following:
1. Rearrange `arr` so it becomes `[1,100,1000]`.
2. Decrease the value of the second element to 2.
3. Decrease the value of the third element to 3.
Now `arr = [1,2,3]`, which` `satisfies the conditions.
The largest element in `arr is 3.`

```

Example 3:**

```

**Input:** arr = [1,2,3,4,5]
**Output:** 5
**Explanation:** The array already satisfies the conditions, and the largest element is 5.

```

 

**Constraints:**

	- `1 <= arr.length <= 10^5`

	- `1 <= arr[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution works by first sorting the array in ascending order. Then, it iterates through the sorted array, starting from the second element (index 1), and increments the maximum value (`maxi`) whenever it encounters a value greater than `maxi`. This approach ensures that the absolute difference between any two adjacent elements is less than or equal to 1, satisfying the problem conditions.

**Approach**
1. Sort the input array `arr` in ascending order using the `sort()` method.
2. Initialize `maxi` to 1, which will store the maximum possible value of an element in the modified array.
3. Iterate through the sorted array, starting from the second element (index 1), using a for loop.
4. For each element `val` in the array, check if it is greater than `maxi`.
5. If `val` is greater than `maxi`, increment `maxi` by 1.
6. After iterating through the entire array, return the final value of `maxi` as the maximum possible value.

**Time Complexity**
O(n log n), where n is the length of the input array. This is because the `sort()` method has a time complexity of O(n log n) in Python.

**Space Complexity**
O(1), excluding the input array. The solution only uses a constant amount of space to store the `maxi` variable.

**Key Insight**
The key insight is that the maximum possible value of an element in the modified array is determined by the number of unique values in the sorted array. By iterating through the sorted array and incrementing `maxi` whenever a new value is encountered, we can efficiently find the maximum possible value. This approach takes advantage of the fact that the array is sorted, allowing us to skip unnecessary comparisons and reduce the time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 11 ms (Beats 95.83%) |
| 💾 Memory | 28.2 MB (Beats 55.56%) |
| 📅 Solved | 2026-06-28 |
| 💻 Language | Python |