# 108. Convert Sorted Array to Binary Search Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Tree](https://img.shields.io/badge/Tree-purple) ![Binary Search Tree](https://img.shields.io/badge/Binary%20Search%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)


## 📝 Problem Description

Given an integer array `nums` where the elements are sorted in **ascending order**, convert *it to a ****height-balanced*** *binary search tree*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg)
```

**Input:** nums = [-10,-3,0,5,9]
**Output:** [0,-3,9,-10,null,5]
**Explanation:** [0,-10,5,null,-3,null,9] is also accepted:
![](https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg)

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/18/btree.jpg)
```

**Input:** nums = [1,3]
**Output:** [3,1]
**Explanation:** [1,null,3] and [3,1] are both height-balanced BSTs.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^4`

	- `-10^4 <= nums[i] <= 10^4`

	- `nums` is sorted in a **strictly increasing** order.

## 🧠 Solution Explanation

## Intuition
This approach works by utilizing a divide-and-conquer strategy to construct a height-balanced binary search tree from a sorted array. The key idea is to select the middle element of the array as the root of the tree, ensuring that the left and right subtrees are also height-balanced. This process is recursively applied to the left and right halves of the array.

## Approach
1. Define a recursive function `bst` that takes two parameters, `l` and `r`, representing the left and right indices of the current array segment.
2. If `l` is greater than `r`, return `None` to indicate an empty subtree.
3. Calculate the middle index `mid` of the current array segment using the formula `(r + l) // 2`.
4. Create a new `TreeNode` with the value at the middle index `mid`.
5. Recursively construct the left and right subtrees by calling `bst` with the updated index ranges `l` to `mid - 1` and `mid + 1` to `r`, respectively.
6. Assign the recursively constructed subtrees to the `left` and `right` attributes of the current node.

## Time Complexity
The time complexity is O(n), where n is the length of the input array. This is because each element in the array is visited exactly once during the recursive construction process.

## Space Complexity
The space complexity is O(log n), which is the maximum depth of the recursive call stack. This is because the recursive function calls are stacked, and the maximum number of simultaneous calls is proportional to the height of the resulting binary search tree, which is logarithmic in the size of the input array.

## Key Insight
The key insight behind this solution is the realization that selecting the middle element of the array as the root of the tree ensures that the resulting binary search tree is height-balanced, which is a crucial property for efficient search and insertion operations. This approach allows for a simple and efficient construction of a height-balanced BST from a sorted array.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 20.3 MB (Beats 29.49%) |
| 📅 Solved | 2026-02-09 |
| 💻 Language | Python |