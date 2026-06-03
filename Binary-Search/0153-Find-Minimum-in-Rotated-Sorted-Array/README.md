> 📌 **Cross-listed:** Primary location is [Array/0153-Find-Minimum-in-Rotated-Sorted-Array](../../Array/0153-Find-Minimum-in-Rotated-Sorted-Array). This problem also appears under: **Array**, **Binary Search**

# 153. Find Minimum in Rotated Sorted Array


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)


## 📝 Problem Description

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

	- `[4,5,6,7,0,1,2]` if it was rotated `4` times.

	- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.

You must write an algorithm that runs in `O(log n) time`.

 

Example 1:**

```

**Input:** nums = [3,4,5,1,2]
**Output:** 1
**Explanation:** The original array was [1,2,3,4,5] rotated 3 times.

```

Example 2:**

```

**Input:** nums = [4,5,6,7,0,1,2]
**Output:** 0
**Explanation:** The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

```

Example 3:**

```

**Input:** nums = [11,13,15,17]
**Output:** 11
**Explanation:** The original array was [11,13,15,17] and it was rotated 4 times. 

```

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 5000`

	- `-5000 <= nums[i] <= 5000`

	- All the integers of `nums` are **unique**.

	- `nums` is sorted and rotated between `1` and `n` times.

## 🧠 Solution Explanation

## Intuition
The solution works by utilizing a modified binary search algorithm to find the minimum element in the rotated sorted array. This approach takes advantage of the fact that the array is sorted in ascending order, but rotated, allowing us to make informed decisions about which half of the array to search. The key idea is to compare the middle element with the leftmost element to determine which half is more likely to contain the minimum element.

## Approach
1. Initialize two pointers, `l` and `r`, to the start and end of the array, respectively.
2. Initialize a variable `mini` to store the minimum element found so far, initially set to the first element of the array.
3. Loop until `l` is greater than `r`.
4. Calculate the middle index `mid` and compare the element at `mid` with the element at `l`.
5. If the element at `l` is less than or equal to the element at `mid`, update `mini` if necessary and move the `l` pointer to `mid + 1`.
6. Otherwise, update `mini` if necessary and move the `r` pointer to `mid - 1`.

## Time Complexity
The time complexity is O(log n), where n is the number of elements in the array. This is because the algorithm divides the search space in half at each step, similar to a standard binary search.

## Space Complexity
The space complexity is O(1), as the algorithm only uses a constant amount of space to store the pointers and the minimum element found so far.

## Key Insight
The key insight behind this solution is the comparison between the middle element and the leftmost element, which allows us to determine which half of the array is more likely to contain the minimum element. This comparison enables us to prune the search space in half at each step, resulting in a logarithmic time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 92.58%) |
| 📅 Solved | 2026-05-15 |
| 💻 Language | Python |