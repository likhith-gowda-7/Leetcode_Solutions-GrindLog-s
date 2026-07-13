# 1291. Sequential Digits


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Enumeration](https://img.shields.io/badge/Enumeration-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sequential-digits/)


## 📝 Problem Description

An integer has *sequential digits* if and only if each digit in the number is one more than the previous digit.

Return a **sorted** list of all the integers in the range `[low, high]` inclusive that have sequential digits.

 

Example 1:**

```
**Input:** low = 100, high = 300
**Output:** [123,234]

```
Example 2:**

```
**Input:** low = 1000, high = 13000
**Output:** [1234,2345,3456,4567,5678,6789,12345]

```

 

**Constraints:**

	- `10 <= low <= high <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The problem requires finding all integers within a given range that have sequential digits. This means each digit in the number is one more than the previous digit. We can leverage the fact that the digits are sequential to generate all possible numbers efficiently.

**Approach**
1. We create a string `seq` containing all digits from 1 to 9.
2. We iterate over all possible start indices `i` for the sequential digits.
3. For each start index `i`, we iterate over all possible end indices `j` that are greater than `i`.
4. We extract the number `num` by taking a substring of `seq` from index `i` to `j` and converting it to an integer.
5. We check if `num` is within the given range `[low, high]`. If it is, we add it to the result list.
6. If `num` exceeds the upper bound `high`, we break the inner loop to avoid unnecessary iterations.
7. Finally, we sort the result list and return it.

**Time Complexity**
O(n*m), where n is the number of possible start indices (10 in this case) and m is the maximum length of the sequential digits (9 in this case). This is because we iterate over all possible start indices and end indices.

**Space Complexity**
O(n*m), where n is the number of possible start indices (10 in this case) and m is the maximum length of the sequential digits (9 in this case). This is because we store all generated numbers in the result list.

**Key Insight**
The key insight is that we can generate all possible sequential digits by iterating over all possible start indices and end indices. This approach allows us to efficiently generate all numbers within the given range that have sequential digits.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 30.59%) |
| 📅 Solved | 2026-07-13 |
| 💻 Language | Python |