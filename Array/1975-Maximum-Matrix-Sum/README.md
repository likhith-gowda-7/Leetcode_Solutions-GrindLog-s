# 1975. Maximum Matrix Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-matrix-sum/)


## 📝 Problem Description

You are given an `n x n` integer `matrix`. You can do the following operation **any** number of times:

	- Choose any two **adjacent** elements of `matrix` and **multiply** each of them by `-1`.

Two elements are considered **adjacent** if and only if they share a **border**.

Your goal is to **maximize** the summation of the matrix's elements. Return *the **maximum** sum of the matrix's elements using the operation mentioned above.*

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex1.png)
```

**Input:** matrix = [[1,-1],[-1,1]]
**Output:** 4
**Explanation:** We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex2.png)
```

**Input:** matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
**Output:** 16
**Explanation:** We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.

```

 

**Constraints:**

	- `n == matrix.length == matrix[i].length`

	- `2 <= n <= 250`

	- `-10^5 <= matrix[i][j] <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution works by first calculating the total sum of the matrix's elements and the number of negative elements. Then, it finds the smallest absolute value of a negative element. If there's an odd number of negative elements, it subtracts twice the smallest absolute value from the total sum to maximize the sum of the matrix's elements.

**Approach**
1. Initialize variables to store the total sum of the matrix's elements, the number of negative elements, and the smallest absolute value of a negative element.
2. Iterate through each element in the matrix, adding its absolute value to the total sum and incrementing the count of negative elements if it's negative.
3. Update the smallest absolute value of a negative element if a smaller one is found.
4. If there's an odd number of negative elements, subtract twice the smallest absolute value from the total sum.
5. Return the total sum as the maximum sum of the matrix's elements.

**Time Complexity**
O(n^2) - The solution iterates through each element in the matrix once, resulting in a time complexity of O(n^2), where n is the number of elements in the matrix.

**Space Complexity**
O(1) - The solution uses a constant amount of space to store the total sum, the number of negative elements, and the smallest absolute value of a negative element, resulting in a space complexity of O(1).

**Key Insight**
The key insight is that by multiplying two adjacent elements by -1, we can change the sum of the matrix by at most 4 (2 for each element). Therefore, to maximize the sum, we should aim to have an even number of negative elements, and if there's an odd number, we should make the smallest absolute value of a negative element as large as possible.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 77 ms (Beats 27.65%) |
| 💾 Memory | 26.9 MB (Beats 100%) |
| 📅 Solved | 2026-01-05 |
| 💻 Language | Python |