> 📌 **Cross-listed:** Primary location is [Array/0912-Sort-an-Array](../../Array/0912-Sort-an-Array). This problem also appears under: **Array**, **Divide and Conquer**, **Sorting**, **Heap (Priority Queue)**, **Merge Sort**, **Bucket Sort**, **Radix Sort**, **Counting Sort**

# 912. Sort an Array


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sort-an-array/)


## 📝 Problem Description

Given an array of integers `nums`, sort the array in ascending order and return it.

You must solve the problem **without using any built-in** functions in `O(nlog(n))` time complexity and with the smallest space complexity possible.

 

Example 1:**

```

**Input:** nums = [5,2,3,1]
**Output:** [1,2,3,5]
**Explanation:** After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

```

Example 2:**

```

**Input:** nums = [5,1,1,2,0,0]
**Output:** [0,0,1,1,2,5]
**Explanation:** Note that the values of nums are not necessarily unique.

```

 

**Constraints:**

	- `1 <= nums.length <= 5 * 10^4`

	- `-5 * 10^4 <= nums[i] <= 5 * 10^4`

## 🧠 Solution Explanation

**Intuition**
The solution uses a heap data structure to sort the array in ascending order. The heap property ensures that the smallest element is always at the root, allowing for efficient extraction and insertion of elements. By repeatedly extracting the smallest element from the heap and adding it to the new sorted array, we can sort the entire array in linear time complexity.

**Approach**
1. Create an empty list `new_arr` to store the sorted elements.
2. Convert the input array `nums` into a heap using `heapq.heapify()`.
3. While the heap is not empty, extract the smallest element from the heap using `heapq.heappop()` and append it to `new_arr`.
4. Repeat step 3 until the heap is empty.
5. Return the sorted array `new_arr`.

**Time Complexity**
O(n log n) - The heapify operation takes O(n) time, and each subsequent heappop operation takes O(log n) time due to the heap property. Since we perform n heappop operations, the overall time complexity is O(n log n).

**Space Complexity**
O(n) - We create a new array `new_arr` to store the sorted elements, which requires O(n) space. The heapify operation modifies the input array in place, so we don't need additional space for the heap.

**Key Insight**
The key insight is that the heap data structure allows us to efficiently extract the smallest element from the array, which is essential for sorting. By using a heap, we can achieve linear time complexity while still meeting the O(n log n) time complexity requirement.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 115 ms (Beats 83.19%) |
| 💾 Memory | 24.6 MB (Beats 99.99%) |
| 📅 Solved | 2025-07-20 |
| 💻 Language | Python |