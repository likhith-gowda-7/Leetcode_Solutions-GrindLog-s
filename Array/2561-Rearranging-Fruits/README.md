# 2561. Rearranging Fruits


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Sort](https://img.shields.io/badge/Sort-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/rearranging-fruits/)


## 📝 Problem Description

You have two fruit baskets containing `n` fruits each. You are given two **0-indexed** integer arrays `basket1` and `basket2` representing the cost of fruit in each basket. You want to make both baskets **equal**. To do so, you can use the following operation as many times as you want:

	- Choose two indices `i` and `j`, and swap the `i^th` fruit of `basket1` with the `j^th` fruit of `basket2`.

	- The cost of the swap is `min(basket1[i], basket2[j])`.

Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.

Return *the minimum cost to make both the baskets equal or *`-1`* if impossible.*

 

Example 1:**

```

**Input:** basket1 = [4,2,2,2], basket2 = [1,4,1,2]
**Output:** 1
**Explanation:** Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.

```

Example 2:**

```

**Input:** basket1 = [2,3,4,1], basket2 = [3,2,5,1]
**Output:** -1
**Explanation:** It can be shown that it is impossible to make both the baskets equal.

```

 

**Constraints:**

	- `basket1.length == basket2.length`

	- `1 <= basket1.length <= 10^5`

	- `1 <= basket1[i], basket2[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution works by first identifying the minimum value in both baskets and maintaining a frequency count of each value. It then checks if it's possible to make both baskets equal by checking if the frequency count of each value is even. If not, it returns -1 as it's impossible to make both baskets equal. If it's possible, it finds the minimum cost by sorting the swapable values and swapping the minimum value with the second minimum value in the sorted list.

**Approach**
1. Initialize a dictionary `freq` to store the frequency count of each value in both baskets.
2. Iterate through both baskets and update the minimum value `min_val` and the frequency count in `freq`.
3. Check if it's possible to make both baskets equal by checking if the frequency count of each value is even. If not, return -1.
4. If it's possible, find the swapable values by iterating through `freq` and adding the value to the list `swapable_values` if its frequency count is even.
5. Sort `swapable_values` in ascending order.
6. Calculate the minimum cost by iterating through the first half of `swapable_values` and swapping the minimum value with the second minimum value in the sorted list.

**Time Complexity**
O(n log n) due to the sorting of `swapable_values` where n is the number of unique values in both baskets.

**Space Complexity**
O(n) where n is the number of unique values in both baskets due to the use of the dictionary `freq` to store the frequency count of each value.

**Key Insight**
The key insight is that if the frequency count of each value is even, it's possible to make both baskets equal by swapping the minimum value with the second minimum value in the sorted list. This is because swapping the minimum value with the second minimum value will not change the sorted order of the values, and since the frequency count of each value is even, we can swap the minimum value with the second minimum value as many times as needed to make both baskets equal.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 135 ms (Beats 10.05%) |
| 💾 Memory | 43.1 MB (Beats 64.55%) |
| 📅 Solved | 2025-08-02 |
| 💻 Language | Python |