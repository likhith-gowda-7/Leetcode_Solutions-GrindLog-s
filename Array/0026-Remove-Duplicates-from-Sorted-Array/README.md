# 26. Remove Duplicates from Sorted Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)


## 📝 Problem Description

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**.

Consider the number of *unique elements* in `nums` to be `k**​​​​​​​**`​​​​​​​. After removing duplicates, return the number of unique elements `k`.

The first `k` elements of `nums` should contain the unique numbers in **sorted order**. The remaining elements beyond index `k - 1` can be ignored.

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

**Input:** nums = [1,1,2]
**Output:** 2, nums = [1,2,_]
**Explanation:** Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

```

Example 2:**

```

**Input:** nums = [0,0,1,1,1,2,2,3,3,4]
**Output:** 5, nums = [0,1,2,3,4,_,_,_,_,_]
**Explanation:** Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

```

 

**Constraints:**

	- `1 <= nums.length <= 3 * 10^4`

	- `-100 <= nums[i] <= 100`

	- `nums` is sorted in **non-decreasing** order.

## 🧠 Solution Explanation

## Intuition
This approach works by utilizing the fact that the input array is sorted in non-decreasing order, allowing us to easily identify and remove duplicates. We maintain a pointer to keep track of the position where the next unique element should be placed. By iterating through the array and comparing adjacent elements, we can efficiently remove duplicates in-place.

## Approach
1. Initialize a pointer `ind` to 1, which will keep track of the position where the next unique element should be placed.
2. Iterate through the array starting from the second element (index 1).
3. For each element, check if it is different from the previous one. If it is, place it at the current `ind` position and increment `ind`.
4. After iterating through the entire array, `ind` will represent the number of unique elements, which is the desired output.

## Time Complexity
The time complexity is O(n), where n is the length of the input array. This is because we are iterating through the array once, performing a constant amount of work for each element.

## Space Complexity
The space complexity is O(1), as we are only using a constant amount of space to store the `ind` pointer and are modifying the input array in-place.

## Key Insight
The key insight behind this solution is the use of the `ind` pointer to keep track of the position where the next unique element should be placed, allowing us to efficiently remove duplicates in-place while maintaining the relative order of the elements. This approach takes advantage of the fact that the input array is sorted, making it possible to solve the problem in linear time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.8 MB (Beats 100%) |
| 📅 Solved | 2025-04-04 |
| 💻 Language | Python |