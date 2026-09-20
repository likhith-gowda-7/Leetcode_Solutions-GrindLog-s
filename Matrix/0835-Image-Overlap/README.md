> 📌 **Cross-listed:** Primary location is [Array/0835-Image-Overlap](../../Array/0835-Image-Overlap). This problem also appears under: **Array**, **Matrix**

# 835. Image Overlap


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/image-overlap/)


## 📝 Problem Description

You are given two images, `img1` and `img2`, represented as binary, square matrices of size `n x n`. A binary matrix has only `0`s and `1`s as values.

We **translate** one image however we choose by sliding all the `1` bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the **overlap** by counting the number of positions that have a `1` in **both** images.

Note also that a translation does **not** include any kind of rotation. Any `1` bits that are translated outside of the matrix borders are erased.

Return *the largest possible overlap*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/09/overlap1.jpg)
```

**Input:** img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
**Output:** 3
**Explanation:** We translate img1 to right by 1 unit and down by 1 unit.
![](https://assets.leetcode.com/uploads/2020/09/09/overlap_step1.jpg)
The number of positions that have a 1 in both images is 3 (shown in red).
![](https://assets.leetcode.com/uploads/2020/09/09/overlap_step2.jpg)

```

Example 2:**

```

**Input:** img1 = [[1]], img2 = [[1]]
**Output:** 1

```

Example 3:**

```

**Input:** img1 = [[0]], img2 = [[0]]
**Output:** 0

```

 

**Constraints:**

	- `n == img1.length == img1[i].length`

	- `n == img2.length == img2[i].length`

	- `1 <= n <= 30`

	- `img1[i][j]` is either `0` or `1`.

	- `img2[i][j]` is either `0` or `1`.

## 🧠 Solution Explanation

**Intuition**  
The overlap after shifting one image is determined solely by how the positions of its `1`s line up with the `1`s of the other image.  
If we look at every pair of `1`s, the vector that moves the first to the second tells us exactly which translation would make those two `1`s overlap. Counting how many pairs share the same vector gives the maximum overlap.

**Approach**  
1. List all coordinates of `1`s in `img1` → `A` and in `img2` → `B`.  
2. Create a 2‑D counter array `cnt` of size `(2n) × (2n)` (shifted by `n` to handle negative offsets).  
3. For each `(ax, ay)` in `A` and each `(bx, by)` in `B`:  
   * Compute the translation vector: `dx = bx - ax + n`, `dy = by - ay + n`.  
   * Increment `cnt[dx][dy]`.  
   * Track the maximum value seen.  
4. Return the maximum count.

**Time Complexity**  
Let `k1` and `k2` be the numbers of `1`s in `img1` and `img2`.  
The double loop runs `k1 × k2` iterations, so the time is **O(k1·k2)**.  
In the worst case `k1, k2 ≤ n²`, giving **O(n⁴)**, but for sparse images it is much faster.

**Space Complexity**  
The counter array uses `(2n)² = O(n²)` space.  
The lists `A` and `B` also use at most `n²` entries each, so overall **O(n²)**.

**Key Insight**  
Every possible translation corresponds to a unique offset between a pair of `1`s. By counting how many pairs produce the same offset, we directly obtain the maximum overlap without explicitly shifting matrices.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 129 ms (Beats 93.42%) |
| 💾 Memory | 19.5 MB (Beats 73.24%) |
| 📅 Solved | 2026-09-13 |
| 💻 Language | Python |