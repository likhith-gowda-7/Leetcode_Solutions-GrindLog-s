> 📌 **Cross-listed:** Primary location is [Hash Table/2103-Rings-and-Rods](../../Hash-Table/2103-Rings-and-Rods). This problem also appears under: **Hash Table**, **String**

# 2103. Rings and Rods


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/rings-and-rods/)


## 📝 Problem Description

There are `n` rings and each ring is either red, green, or blue. The rings are distributed **across ten rods** labeled from `0` to `9`.

You are given a string `rings` of length `2n` that describes the `n` rings that are placed onto the rods. Every two characters in `rings` forms a **color-position pair** that is used to describe each ring where:

	- The **first** character of the `i^th` pair denotes the `i^th` ring's **color** (`'R'`, `'G'`, `'B'`).

	- The **second** character of the `i^th` pair denotes the **rod** that the `i^th` ring is placed on (`'0'` to `'9'`).

For example, `"R3G2B1"` describes `n == 3` rings: a red ring placed onto the rod labeled 3, a green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.

Return *the number of rods that have **all three colors** of rings on them.*

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/11/23/ex1final.png)
```

**Input:** rings = "B0B6G0R6R0R6G9"
**Output:** 1
**Explanation:** 
- The rod labeled 0 holds 3 rings with all colors: red, green, and blue.
- The rod labeled 6 holds 3 rings, but it only has red and blue.
- The rod labeled 9 holds only a green ring.
Thus, the number of rods with all three colors is 1.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/11/23/ex2final.png)
```

**Input:** rings = "B0R0G0R9R0B0G0"
**Output:** 1
**Explanation:** 
- The rod labeled 0 holds 6 rings with all colors: red, green, and blue.
- The rod labeled 9 holds only a red ring.
Thus, the number of rods with all three colors is 1.

```

Example 3:**

```

**Input:** rings = "G4"
**Output:** 0
**Explanation:** 
Only one ring is given. Thus, no rods have all three colors.

```

 

**Constraints:**

	- `rings.length == 2 * n`

	- `1 <= n <= 100`

	- `rings[i]` where `i` is **even** is either `'R'`, `'G'`, or `'B'` (**0-indexed**).

	- `rings[i]` where `i` is **odd** is a digit from `'0'` to `'9'` (**0-indexed**).

## 🧠 Solution Explanation

**Intuition**
The solution works by first creating a hash table where the keys are the rod numbers and the values are sets of colors placed on those rods. Then, it iterates through the hash table values and counts the number of rods that have all three colors.

**Approach**
1. Create an empty hash table `h1` with default values as sets.
2. Iterate through the input string `rings` in steps of 2, where each pair of characters represents a color-position pair.
3. For each pair, extract the color (`col`) and rod number (`rod`), and add the color to the set of colors for the corresponding rod in the hash table.
4. Initialize a count variable to 0.
5. Iterate through the values of the hash table, and for each set of colors, check if it has exactly 3 elements (i.e., all three colors). If it does, increment the count.
6. Return the count.

**Time Complexity**
O(n), where n is the length of the input string `rings`. This is because we iterate through the string once to populate the hash table, and then iterate through the hash table values once to count the rods with all three colors.

**Space Complexity**
O(n), where n is the length of the input string `rings`. This is because in the worst case, we might need to store all colors in the hash table.

**Key Insight**
The key insight is that we can use a hash table to efficiently store and query the colors on each rod. By using sets as values, we can easily check if a rod has all three colors by checking the size of the set. This approach allows us to solve the problem in linear time and space.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-02-11 |
| 💻 Language | Python |