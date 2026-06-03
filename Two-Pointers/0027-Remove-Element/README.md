> 📌 **Cross-listed:** Primary location is [Array/0027-Remove-Element](../../Array/0027-Remove-Element). This problem also appears under: **Array**, **Two Pointers**

# 27. Remove Element


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/remove-element/)


## 📝 Problem Description

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm). The order of the elements may be changed. Then return *the number of elements in *`nums`* which are not equal to *`val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

	- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.

	- Return `k`.

**Custom Judge:**

The judge will test your solution with the following code:

```

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}

```

If all assertions pass, then your solution will be **accepted**.

 

Example 1:**

```

**Input:** nums = [3,2,2,3], val = 3
**Output:** 2, nums = [2,2,_,_]
**Explanation:** Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

```

Example 2:**

```

**Input:** nums = [0,1,2,2,3,0,4,2], val = 2
**Output:** 5, nums = [0,1,4,0,3,_,_,_]
**Explanation:** Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

```

 

**Constraints:**

	- `0 <= nums.length <= 100`

	- `0 <= nums[i] <= 50`

	- `0 <= val <= 100`

## 🧠 Solution Explanation

## Intuition
This approach works by utilizing a two-pointer technique to iterate through the array and replace elements that are not equal to the target value. The intuition behind this is to maintain a separate index that keeps track of the position where the next non-target element should be placed. By doing so, we can efficiently remove all occurrences of the target value in-place.

## Approach
1. Initialize an index `ind` to 0, which will keep track of the position where the next non-target element should be placed.
2. Iterate through the array using a for loop, checking each element to see if it's not equal to the target value `val`.
3. If an element is not equal to `val`, place it at the current `ind` position and increment `ind`.
4. After iterating through the entire array, `ind` will represent the number of elements that are not equal to `val`, and the first `ind` elements of the array will contain these non-target elements.

## Time Complexity
The time complexity is O(n), where n is the number of elements in the array, because we are iterating through the array once.

## Space Complexity
The space complexity is O(1), because we are only using a constant amount of space to store the index `ind` and are modifying the input array in-place.

## Key Insight
The key insight behind this solution is the use of a separate index `ind` to keep track of the position where the next non-target element should be placed, allowing us to efficiently remove all occurrences of the target value in-place without using any additional space that scales with the input size.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.1 MB (Beats 88%) |
| 📅 Solved | 2026-03-13 |
| 💻 Language | Python |