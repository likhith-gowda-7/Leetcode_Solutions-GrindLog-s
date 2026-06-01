# 654. Maximum Binary Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Tree](https://img.shields.io/badge/Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-binary-tree/)


## 📝 Problem Description

You are given an integer array `nums` with no duplicates. A **maximum binary tree** can be built recursively from `nums` using the following algorithm:

	- Create a root node whose value is the maximum value in `nums`.

	- Recursively build the left subtree on the **subarray prefix** to the **left** of the maximum value.

	- Recursively build the right subtree on the **subarray suffix** to the **right** of the maximum value.

Return *the **maximum binary tree** built from *`nums`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/24/tree1.jpg)
```

**Input:** nums = [3,2,1,6,0,5]
**Output:** [6,3,5,null,2,0,null,null,1]
**Explanation:** The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/12/24/tree2.jpg)
```

**Input:** nums = [3,2,1]
**Output:** [3,null,2,null,1]

```

 

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `0 <= nums[i] <= 1000`

	- All integers in `nums` are **unique**.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 31 ms (Beats 55.59%) |
| 💾 Memory | 18.4 MB (Beats 100%) |
| 📅 Solved | 2025-06-07 |
| 💻 Language | Python |