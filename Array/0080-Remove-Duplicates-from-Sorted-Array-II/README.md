# 80. Remove Duplicates from Sorted Array II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)


## 📝 Problem Description

Given an integer array `nums` sorted in **non-decreasing order**, remove some duplicates [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that each unique element appears **at most twice**. The **relative order** of the elements should be kept the **same**.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k`* after placing the final result in the first *`k`* slots of *`nums`.

Do **not** allocate extra space for another array. You must do this by **modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** with O(1) extra memory.

**Custom Judge:**

The judge will test your solution with the following code:

```

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

```

If all assertions pass, then your solution will be **accepted**.

 

Example 1:**

```

**Input:** nums = [1,1,1,2,2,3]
**Output:** 5, nums = [1,1,2,2,3,_]
**Explanation:** Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

```

Example 2:**

```

**Input:** nums = [0,0,1,1,1,1,2,3,3]
**Output:** 7, nums = [0,0,1,1,2,3,3,_,_]
**Explanation:** Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

```

 

**Constraints:**

	- `1 <= nums.length <= 3 * 10^4`

	- `-10^4 <= nums[i] <= 10^4`

	- `nums` is sorted in **non-decreasing** order.

## 🧠 Solution Explanation

## Intuition
This solution works by iterating through the sorted array and maintaining a count of consecutive duplicates. It utilizes two pointers, `i` and `j`, where `i` keeps track of the position to place the next unique element (or its second occurrence), and `j` is used to traverse the array. By only incrementing `i` when a new element or its second occurrence is found, we effectively remove duplicates while preserving the relative order.

## Approach
1. Initialize two pointers, `i` and `j`, to 1, and a counter `c` to 1, which tracks the count of consecutive duplicates.
2. Iterate through the array using `j`, starting from the second element.
3. If the current element is the same as the previous one, increment `c`. Otherwise, reset `c` to 1.
4. If `c` is less than or equal to 2, place the current element at the `i-th` position and increment `i`.
5. After iterating through the entire array, `i` will represent the number of elements in the modified array.

## Time Complexity
The time complexity is O(n), where n is the number of elements in the array, since we are making a single pass through the array.

## Space Complexity
The space complexity is O(1), as we are only using a constant amount of space to store the pointers and the counter, and we are modifying the input array in-place.

## Key Insight
The key insight here is the use of two pointers, `i` and `j`, to separate the concerns of iterating through the array and placing the unique elements (or their second occurrences) in the correct positions, allowing for an efficient and space-effective solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 46 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-01-04 |
| 💻 Language | Python |