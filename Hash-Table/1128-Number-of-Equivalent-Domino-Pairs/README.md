> 📌 **Cross-listed:** Primary location is [Array/1128-Number-of-Equivalent-Domino-Pairs](../../Array/1128-Number-of-Equivalent-Domino-Pairs). This problem also appears under: **Array**, **Hash Table**, **Counting**

# 1128. Number of Equivalent Domino Pairs


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-equivalent-domino-pairs/)


## 📝 Problem Description

Given a list of `dominoes`, `dominoes[i] = [a, b]` is **equivalent to** `dominoes[j] = [c, d]` if and only if either (`a == c` and `b == d`), or (`a == d` and `b == c`) - that is, one domino can be rotated to be equal to another domino.

Return *the number of pairs *`(i, j)`* for which *`0 <= i < j < dominoes.length`*, and *`dominoes[i]`* is **equivalent to** *`dominoes[j]`.

 

Example 1:**

```

**Input:** dominoes = [[1,2],[2,1],[3,4],[5,6]]
**Output:** 1

```

Example 2:**

```

**Input:** dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
**Output:** 3

```

 

**Constraints:**

	- `1 <= dominoes.length <= 4 * 10^4`

	- `dominoes[i].length == 2`

	- `1 <= dominoes[i][j] <= 9`

## 🧠 Solution Explanation

**Intuition**
The solution works by treating each domino as a unique pair of numbers, and then using a hash table to count the occurrences of each pair. The key insight is that we can rotate each domino to create a reversed pair, and then use the hash table to count the occurrences of both the original and reversed pairs.

**Approach**
1. Initialize an empty hash table `h1` to store the counts of each pair.
2. Iterate through each domino `dom` in the input list `dominoes`.
3. Convert the domino to a tuple `tup` to make it hashable.
4. Check if the tuple `tup` is already in the hash table `h1`. If it is, add the previous count to the total count `count`.
5. Check if the reversed tuple `tup[::-1]` is in the hash table `h1`. If it is, add the previous count to the total count `count`, and increment the count of the reversed tuple in the hash table.
6. If neither the original nor reversed tuple is in the hash table, add the tuple to the hash table with a count of 1.
7. Return the total count `count` at the end of the iteration.

**Time Complexity**
The time complexity of this solution is O(n), where n is the number of dominoes. This is because we are iterating through each domino once, and the operations inside the loop (hash table lookups and updates) take constant time.

**Space Complexity**
The space complexity of this solution is O(n), where n is the number of dominoes. This is because in the worst case, we may need to store all dominoes in the hash table.

**Key Insight**
The key insight is that we can rotate each domino to create a reversed pair, and then use the hash table to count the occurrences of both the original and reversed pairs. This allows us to count the number of equivalent pairs in a single pass through the input list.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 8 ms (Beats 62.02%) |
| 💾 Memory | 24.3 MB (Beats 100%) |
| 📅 Solved | 2025-05-04 |
| 💻 Language | Python |