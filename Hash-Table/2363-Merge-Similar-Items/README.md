> 📌 **Cross-listed:** Primary location is [Array/2363-Merge-Similar-Items](../../Array/2363-Merge-Similar-Items). This problem also appears under: **Array**, **Hash Table**, **Sorting**, **Ordered Set**

# 2363. Merge Similar Items


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Ordered Set](https://img.shields.io/badge/Ordered%20Set-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/merge-similar-items/)


## 📝 Problem Description

You are given two 2D integer arrays, `items1` and `items2`, representing two sets of items. Each array `items` has the following properties:

	- `items[i] = [value_i, weight_i]` where `value_i` represents the **value** and `weight_i` represents the **weight **of the `i^th` item.

	- The value of each item in `items` is **unique**.

Return *a 2D integer array* `ret` *where* `ret[i] = [value_i, weight_i]`*,* *with* `weight_i` *being the **sum of weights** of all items with value* `value_i`.

**Note:** `ret` should be returned in **ascending** order by value.

 

Example 1:**

```

**Input:** items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
**Output:** [[1,6],[3,9],[4,5]]
**Explanation:** 
The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 5, total weight = 1 + 5 = 6.
The item with value = 3 occurs in items1 with weight = 8 and in items2 with weight = 1, total weight = 8 + 1 = 9.
The item with value = 4 occurs in items1 with weight = 5, total weight = 5.  
Therefore, we return [[1,6],[3,9],[4,5]].

```

Example 2:**

```

**Input:** items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]
**Output:** [[1,4],[2,4],[3,4]]
**Explanation:** 
The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 3, total weight = 1 + 3 = 4.
The item with value = 2 occurs in items1 with weight = 3 and in items2 with weight = 1, total weight = 3 + 1 = 4.
The item with value = 3 occurs in items1 with weight = 2 and in items2 with weight = 2, total weight = 2 + 2 = 4.
Therefore, we return [[1,4],[2,4],[3,4]].
```

Example 3:**

```

**Input:** items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]]
**Output:** [[1,7],[2,4],[7,1]]
**Explanation:
**The item with value = 1 occurs in items1 with weight = 3 and in items2 with weight = 4, total weight = 3 + 4 = 7. 
The item with value = 2 occurs in items1 with weight = 2 and in items2 with weight = 2, total weight = 2 + 2 = 4. 
The item with value = 7 occurs in items2 with weight = 1, total weight = 1.
Therefore, we return [[1,7],[2,4],[7,1]].

```

 

**Constraints:**

	- `1 <= items1.length, items2.length <= 1000`

	- `items1[i].length == items2[i].length == 2`

	- `1 <= value_i, weight_i <= 1000`

	- Each `value_i` in `items1` is **unique**.

	- Each `value_i` in `items2` is **unique**.

## 🧠 Solution Explanation

**Intuition**
The solution utilizes a hash table to efficiently store and sum up the weights of items with the same value. This approach allows for a simple and scalable way to merge the two sets of items.

**Approach**
1. Initialize an empty list `res` to store the merged items and a hash table `h1` to store the sum of weights for each item value.
2. Iterate through the combined list of items from both `items1` and `items2`, incrementing the weight value in the hash table `h1` for each item value.
3. Iterate through the hash table `h1` and append each item value and its corresponding weight to the `res` list.
4. Sort the `res` list in ascending order by item value.

**Time Complexity**
The time complexity of this solution is O(n log n) due to the sorting operation in the final step, where n is the total number of items across both input arrays. The initial iteration through the combined list of items is O(n) and the iteration through the hash table is also O(n), but these operations are dominated by the sorting step.

**Space Complexity**
The space complexity of this solution is O(n), where n is the total number of items across both input arrays. This is because we are storing the merged items in the `res` list and the hash table `h1`.

**Key Insight**
The key insight behind this solution is the use of a hash table to efficiently store and sum up the weights of items with the same value. This allows us to avoid duplicate calculations and simplify the merging process, making the solution scalable for large input arrays.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 83.18%) |
| 💾 Memory | 18.7 MB (Beats 100%) |
| 📅 Solved | 2025-02-08 |
| 💻 Language | Python |