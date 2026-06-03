# 868. Binary Gap


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/binary-gap/)


## 📝 Problem Description

Given a positive integer `n`, find and return *the **longest distance** between any two **adjacent** *`1`*'s in the binary representation of *`n`*. If there are no two adjacent *`1`*'s, return *`0`*.*

Two `1`'s are **adjacent** if there are only `0`'s separating them (possibly no `0`'s). The **distance** between two `1`'s is the absolute difference between their bit positions. For example, the two `1`'s in `"1001"` have a distance of 3.

 

Example 1:**

```

**Input:** n = 22
**Output:** 2
**Explanation:** 22 in binary is "10110".
The first adjacent pair of 1's is "10110" with a distance of 2.
The second adjacent pair of 1's is "10110" with a distance of 1.
The answer is the largest of these two distances, which is 2.
Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.

```

Example 2:**

```

**Input:** n = 8
**Output:** 0
**Explanation:** 8 in binary is "1000".
There are not any adjacent pairs of 1's in the binary representation of 8, so we return 0.

```

Example 3:**

```

**Input:** n = 5
**Output:** 2
**Explanation:** 5 in binary is "101".

```

 

**Constraints:**

	- `1 <= n <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution works by first converting the input number to its binary representation. It then iterates through the binary string, keeping track of the position of the last '1' encountered. Whenever it finds another '1', it calculates the distance between the current '1' and the previous one, updating the maximum distance found so far.

**Approach**
1. Convert the input number `n` to its binary representation using the `bin()` function and remove the '0b' prefix.
2. If the binary string contains less than two '1's, return 0 as there are no adjacent '1's.
3. Initialize `prev` to 100 (a value larger than any possible index) if the first character of the binary string is not '1', otherwise set it to 0.
4. Initialize `res` to 0 to store the maximum distance found so far.
5. Iterate through the binary string starting from the second character (index 1).
6. If the current character is '1', calculate the distance between the current '1' and the previous one by subtracting `prev` from the current index `i`.
7. Update `res` with the maximum of its current value and the calculated distance.
8. Update `prev` to the current index `i`.
9. Return `res` at the end of the iteration.

**Time Complexity**
O(log(n)) where n is the input number. This is because the binary representation of n has a maximum length of log2(n) + 1, and we iterate through this string once.

**Space Complexity**
O(log(n)) as we need to store the binary representation of n, which has a maximum length of log2(n) + 1.

**Key Insight**
The key insight is to keep track of the position of the last '1' encountered, allowing us to efficiently calculate the distance between adjacent '1's. This approach avoids the need to store the positions of all '1's, making it more space-efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.6 MB (Beats 12.01%) |
| 📅 Solved | 2026-02-22 |
| 💻 Language | Python |