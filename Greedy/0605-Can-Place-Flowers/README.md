> 📌 **Cross-listed:** Primary location is [Array/0605-Can-Place-Flowers](../../Array/0605-Can-Place-Flowers). This problem also appears under: **Array**, **Greedy**

# 605. Can Place Flowers


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/can-place-flowers/)


## 📝 Problem Description

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in **adjacent** plots.

Given an integer array `flowerbed` containing `0`'s and `1`'s, where `0` means empty and `1` means not empty, and an integer `n`, return `true` *if* `n` *new flowers can be planted in the* `flowerbed` *without violating the no-adjacent-flowers rule and* `false` *otherwise*.

 

Example 1:**

```
**Input:** flowerbed = [1,0,0,0,1], n = 1
**Output:** true

```
Example 2:**

```
**Input:** flowerbed = [1,0,0,0,1], n = 2
**Output:** false

```

 

**Constraints:**

	- `1 <= flowerbed.length <= 2 * 10^4`

	- `flowerbed[i]` is `0` or `1`.

	- There are no two adjacent flowers in `flowerbed`.

	- `0 <= n <= flowerbed.length`

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through the flowerbed and planting a new flower in each empty plot that is not adjacent to another flower. The key insight is that we can plant a new flower in an empty plot if and only if it is not adjacent to any other flower.

**Approach**
1. Initialize two variables `prev` and `nex` to keep track of the previous and next plot in the flowerbed.
2. Iterate through the flowerbed from left to right.
3. For each empty plot (i.e., `flowerbed[i] == 0`), check if it is not adjacent to any other flower by verifying that `prev` and `nex` are both 0.
4. If the plot is not adjacent to any other flower and we still have flowers to plant (`n > 0`), plant a new flower in the plot by setting `flowerbed[i] = 1` and decrementing `n`.
5. If we have planted all the required flowers (`n == 0`), return `True`.
6. If we have iterated through the entire flowerbed and still have flowers to plant, return `False`.

**Time Complexity**
The time complexity of this solution is O(n), where n is the length of the flowerbed. This is because we are iterating through the flowerbed once.

**Space Complexity**
The space complexity of this solution is O(1), which means the space required does not grow with the size of the input. This is because we are only using a constant amount of space to store the variables `prev`, `nex`, and `n`.

**Key Insight**
The key insight is that we can plant a new flower in an empty plot if and only if it is not adjacent to any other flower. This allows us to efficiently iterate through the flowerbed and determine whether we can plant all the required flowers.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 79.52%) |
| 💾 Memory | 17.6 MB (Beats 100%) |
| 📅 Solved | 2024-12-05 |
| 💻 Language | Python |