# 1622. Fancy Sequence


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Design](https://img.shields.io/badge/Design-purple) ![Segment Tree](https://img.shields.io/badge/Segment%20Tree-purple) ![Number Theory](https://img.shields.io/badge/Number%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/fancy-sequence/)


## 📝 Problem Description

Write an API that generates fancy sequences using the `append`, `addAll`, and `multAll` operations.

Implement the `Fancy` class:

	- `Fancy()` Initializes the object with an empty sequence.

	- `void append(val)` Appends an integer `val` to the end of the sequence.

	- `void addAll(inc)` Increments all existing values in the sequence by an integer `inc`.

	- `void multAll(m)` Multiplies all existing values in the sequence by an integer `m`.

	- `int getIndex(idx)` Gets the current value at index `idx` (0-indexed) of the sequence **modulo** `10^9 + 7`. If the index is greater or equal than the length of the sequence, return `-1`.

 

Example 1:**

```

**Input**
["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
**Output**
[null, null, null, null, null, 10, null, null, null, 26, 34, 20]

**Explanation**
Fancy fancy = new Fancy();
fancy.append(2);   // fancy sequence: [2]
fancy.addAll(3);   // fancy sequence: [2+3] -> [5]
fancy.append(7);   // fancy sequence: [5, 7]
fancy.multAll(2);  // fancy sequence: [5*2, 7*2] -> [10, 14]
fancy.getIndex(0); // return 10
fancy.addAll(3);   // fancy sequence: [10+3, 14+3] -> [13, 17]
fancy.append(10);  // fancy sequence: [13, 17, 10]
fancy.multAll(2);  // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
fancy.getIndex(0); // return 26
fancy.getIndex(1); // return 34
fancy.getIndex(2); // return 20

```

 

**Constraints:**

	- `1 <= val, inc, m <= 100`

	- `0 <= idx <= 10^5`

	- At most `10^5` calls total will be made to `append`, `addAll`, `multAll`, and `getIndex`.

## 🧠 Solution Explanation

**Intuition**
The Fancy class uses a combination of modular arithmetic and exponentiation by squaring to efficiently handle the `append`, `addAll`, and `multAll` operations. By storing the intermediate results and using modular arithmetic, we can avoid dealing with large numbers and achieve a constant time complexity for these operations.

**Approach**
1. Initialize an empty list `nums` to store the sequence values, and two variables `adds` and `multi` to track the cumulative sum and product of the sequence, respectively.
2. Implement the `power` function to efficiently compute the modular exponentiation using exponentiation by squaring.
3. In the `append` method, calculate the new value by applying the modular arithmetic formula: `(val - adds) % mod + mod`, then multiply the result by `multi` using the `power` function, and append the result to `nums`.
4. In the `addAll` method, simply update `adds` by adding `inc` modulo `mod`.
5. In the `multAll` method, update both `adds` and `multi` by multiplying them with `m` modulo `mod`.
6. In the `getIndex` method, return the value at index `idx` by multiplying the corresponding value in `nums` with `multi`, adding `adds`, and taking the result modulo `mod`. If `idx` is out of bounds, return `-1`.

**Time Complexity**
The time complexity of the `append`, `addAll`, and `multAll` operations is O(1), as they involve constant-time modular arithmetic and exponentiation by squaring. The `getIndex` method also has a time complexity of O(1), as it simply accesses the corresponding value in `nums` and performs some constant-time calculations.

**Space Complexity**
The space complexity is O(n), where n is the number of `append` operations, as we store the sequence values in the `nums` list.

**Key Insight**
The key insight is to use modular arithmetic to avoid dealing with large numbers, and to use exponentiation by squaring to efficiently compute the modular exponentiation. By storing the intermediate results and using these techniques, we can achieve a constant time complexity for the `append`, `addAll`, and `multAll` operations.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 416 ms (Beats 19.46%) |
| 💾 Memory | 54.2 MB (Beats 95.42%) |
| 📅 Solved | 2026-03-15 |
| 💻 Language | Python |