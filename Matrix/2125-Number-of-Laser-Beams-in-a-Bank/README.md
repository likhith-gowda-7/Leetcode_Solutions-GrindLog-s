> 📌 **Cross-listed:** Primary location is [Array/2125-Number-of-Laser-Beams-in-a-Bank](../../Array/2125-Number-of-Laser-Beams-in-a-Bank). This problem also appears under: **Array**, **Math**, **String**, **Matrix**

# 2125. Number of Laser Beams in a Bank


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![String](https://img.shields.io/badge/String-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/)


## 📝 Problem Description

Anti-theft security devices are activated inside a bank. You are given a **0-indexed** binary string array `bank` representing the floor plan of the bank, which is an `m x n` 2D matrix. `bank[i]` represents the `i^th` row, consisting of `'0'`s and `'1'`s. `'0'` means the cell is empty, while`'1'` means the cell has a security device.

There is **one** laser beam between any **two** security devices **if both** conditions are met:

	- The two devices are located on two **different rows**: `r_1` and `r_2`, where `r_1 < r_2`.

	- For **each** row `i` where `r_1 < i < r_2`, there are **no security devices** in the `i^th` row.

Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return *the total number of laser beams in the bank*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/12/24/laser1.jpg)
```

**Input:** bank = ["011001","000000","010100","001000"]
**Output:** 8
**Explanation:** Between each of the following device pairs, there is one beam. In total, there are 8 beams:
 * bank[0][1] -- bank[2][1]
 * bank[0][1] -- bank[2][3]
 * bank[0][2] -- bank[2][1]
 * bank[0][2] -- bank[2][3]
 * bank[0][5] -- bank[2][1]
 * bank[0][5] -- bank[2][3]
 * bank[2][1] -- bank[3][2]
 * bank[2][3] -- bank[3][2]
Note that there is no beam between any device on the 0^th row with any on the 3^rd row.
This is because the 2^nd row contains security devices, which breaks the second condition.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/12/24/laser2.jpg)
```

**Input:** bank = ["000","111","000"]
**Output:** 0
**Explanation:** There does not exist two devices located on two different rows.

```

 

**Constraints:**

	- `m == bank.length`

	- `n == bank[i].length`

	- `1 <= m, n <= 500`

	- `bank[i][j]` is either `'0'` or `'1'`.

## 🧠 Solution Explanation

**Intuition**
The solution works by first counting the number of security devices (represented by '1's) in each row of the bank. Then, it iterates over the counts, multiplying each count with the previous one to calculate the number of laser beams that can be formed between the devices in the current and previous rows.

**Approach**
1. Initialize an empty list `cams` to store the counts of security devices in each row.
2. Iterate over each row `floor` in the bank, counting the number of security devices using `floor.count("1")`.
3. If the count is greater than 0, append it to the `cams` list.
4. Initialize a variable `total` to 0, which will store the total number of laser beams.
5. Iterate over the `cams` list, starting from the second element (index 1). For each element `cams[i]`, multiply it with the previous element `cams[i-1]` and add the result to `total`.
6. Return the total number of laser beams.

**Time Complexity**
O(m + n), where m is the number of rows and n is the maximum number of security devices in a row. This is because we iterate over each row once and count the security devices in each row.

**Space Complexity**
O(m), where m is the number of rows. This is because we store the counts of security devices in each row in the `cams` list.

**Key Insight**
The key insight is that the number of laser beams between two rows is equal to the product of the number of security devices in those two rows. This is because each security device in the first row can form a laser beam with each security device in the second row, resulting in a total of `cams[i-1] * cams[i]` laser beams.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.7 MB (Beats 100%) |
| 📅 Solved | 2025-10-27 |
| 💻 Language | Python |