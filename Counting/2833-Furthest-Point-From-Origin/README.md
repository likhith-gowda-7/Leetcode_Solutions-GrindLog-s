> 📌 **Cross-listed:** Primary location is [String/2833-Furthest-Point-From-Origin](../../String/2833-Furthest-Point-From-Origin). This problem also appears under: **String**, **Counting**

# 2833. Furthest Point From Origin


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/furthest-point-from-origin/)


## 📝 Problem Description

You are given a string `moves` of length `n` consisting only of characters `'L'`, `'R'`, and `'_'`. The string represents your movement on a number line starting from the origin `0`.

In the `i^th` move, you can choose one of the following directions:

	- move to the left if `moves[i] = 'L'` or `moves[i] = '_'`

	- move to the right if `moves[i] = 'R'` or `moves[i] = '_'`

Return *the **distance from the origin** of the **furthest** point you can get to after *`n`* moves*.

 

Example 1:**

```

**Input:** moves = "L_RL__R"
**Output:** 3
**Explanation:** The furthest point we can reach from the origin 0 is point -3 through the following sequence of moves "LLRLLLR".

```

Example 2:**

```

**Input:** moves = "_R__LL_"
**Output:** 5
**Explanation:** The furthest point we can reach from the origin 0 is point -5 through the following sequence of moves "LRLLLLL".

```

Example 3:**

```

**Input:** moves = "_______"
**Output:** 7
**Explanation:** The furthest point we can reach from the origin 0 is point 7 through the following sequence of moves "RRRRRRR".

```

 

**Constraints:**

	- `1 <= moves.length == n <= 50`

	- `moves` consists only of characters `'L'`, `'R'` and `'_'`.

## 🧠 Solution Explanation

**Intuition**
The solution works by counting the number of left and right moves, as well as the number of neutral moves (represented by '_'). The furthest point from the origin can be achieved by taking all the right moves and neutral moves, while discarding the left moves. The key idea is to maximize the number of moves to the right.

**Approach**
1. Count the number of left moves (`left_count`) and right moves (`right_count`) in the given string.
2. Count the number of neutral moves (`choices_count`) in the given string.
3. Calculate the maximum distance that can be achieved by taking all right moves and neutral moves, and discarding left moves.
4. Return the calculated distance.

**Time Complexity**
O(n), where n is the length of the input string `moves`. This is because we are using the `count` method, which iterates over the string once.

**Space Complexity**
O(1), as we are only using a constant amount of space to store the counts of left, right, and neutral moves.

**Key Insight**
The key insight is that the furthest point from the origin can be achieved by taking all the right moves and neutral moves, while discarding the left moves. This is because the neutral moves can be used to move either left or right, and taking all right moves maximizes the distance from the origin.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.4 MB (Beats 18.11%) |
| 📅 Solved | 2026-04-24 |
| 💻 Language | Python |