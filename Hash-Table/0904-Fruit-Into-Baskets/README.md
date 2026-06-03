> 📌 **Cross-listed:** Primary location is [Array/0904-Fruit-Into-Baskets](../../Array/0904-Fruit-Into-Baskets). This problem also appears under: **Array**, **Hash Table**, **Sliding Window**

# 904. Fruit Into Baskets


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/fruit-into-baskets/)


## 📝 Problem Description

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the **type** of fruit the `i^th` tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

	- You only have **two** baskets, and each basket can only hold a **single type** of fruit. There is no limit on the amount of fruit each basket can hold.

	- Starting from any tree of your choice, you must pick **exactly one fruit** from **every** tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.

	- Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array `fruits`, return *the **maximum** number of fruits you can pick*.

 

Example 1:**

```

**Input:** fruits = [1,2,1]
**Output:** 3
**Explanation:** We can pick from all 3 trees.

```

Example 2:**

```

**Input:** fruits = [0,1,2,2]
**Output:** 3
**Explanation:** We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

```

Example 3:**

```

**Input:** fruits = [1,2,3,2,2]
**Output:** 4
**Explanation:** We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].

```

 

**Constraints:**

	- `1 <= fruits.length <= 10^5`

	- `0 <= fruits[i] < fruits.length`

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach with two pointers, `l` and `r`, to traverse the array of fruits. The key insight is to maintain a bucket (hash map) that keeps track of the types of fruits in the current window. By ensuring that the bucket size is at most 2, we can collect as much fruit as possible while adhering to the problem constraints.

**Approach**
1. Initialize the result (`res`) to 0, a bucket (hash map) to store the types of fruits, and two pointers (`l` and `r`) to the start and end of the window.
2. Iterate through the array of fruits with the `r` pointer.
3. If the current fruit is not in the bucket, update the result with the maximum window size seen so far and slide the window to the right by incrementing the `l` pointer until the bucket size is 2.
4. Add the current fruit to the bucket and update its count.
5. After the iteration, update the result with the maximum window size seen at the end of the array.

**Time Complexity**
O(n), where n is the length of the array of fruits. This is because we iterate through the array once with the `r` pointer and perform constant-time operations for each fruit.

**Space Complexity**
O(n), where n is the length of the array of fruits. In the worst case, we need to store all the unique fruits in the bucket.

**Key Insight**
The key to this solution is to maintain a bucket size of at most 2, which allows us to collect as much fruit as possible while adhering to the problem constraints. By sliding the window to the right and updating the bucket accordingly, we can efficiently find the maximum window size that satisfies the problem conditions.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 132 ms (Beats 92.11%) |
| 💾 Memory | 23.6 MB (Beats 100%) |
| 📅 Solved | 2025-08-04 |
| 💻 Language | Python |