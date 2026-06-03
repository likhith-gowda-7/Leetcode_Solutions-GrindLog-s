> 📌 **Cross-listed:** Primary location is [String/1111-Maximum-Nesting-Depth-of-Two-Valid-Parentheses-Strings](../../String/1111-Maximum-Nesting-Depth-of-Two-Valid-Parentheses-Strings). This problem also appears under: **String**, **Stack**

# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/)


## 📝 Problem Description

A string is a *valid parentheses string* (denoted VPS) if and only if it consists of `"("` and `")"` characters only, and:

	- It is the empty string, or

	- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are VPS's, or

	- It can be written as `(A)`, where `A` is a VPS.

We can similarly define the *nesting depth* `depth(S)` of any VPS `S` as follows:

	- `depth("") = 0`

	- `depth(A + B) = max(depth(A), depth(B))`, where `A` and `B` are VPS's

	- `depth("(" + A + ")") = 1 + depth(A)`, where `A` is a VPS.

For example, `""`, `"()()"`, and `"()(()())"` are VPS's (with nesting depths 0, 1, and 2), and `")("` and `"(()"` are not VPS's.

Given a VPS seq, split it into two disjoint subsequences `A` and `B`, such that `A` and `B` are VPS's (and `A.length + B.length = seq.length`). The subsequences may not necessarily be contiguous.

For example, for the sequence `123456789`, one possible split is:

	
	A = {1, 3, 5, 7, 9}`,

	

	
	B = {2, 4, 6, 8}`.

	

This corresponds to the output `[0, 1, 0, 1, 0, 1, 0, 1, 0]`  where 0 indicates membership in A` and 1 indicates membership in B`.

Now choose **any** such `A` and `B` such that `max(depth(A), depth(B))` is the minimum possible value.

Return an `answer` array (of length `seq.length`) that encodes such a choice of `A` and `B`:  `answer[i] = 0` if `seq[i]` is part of `A`, else `answer[i] = 1`.  Note that even though multiple answers may exist, you may return any of them.

 

Example 1:**

```

**Input:** seq = "(()())"
**Output:** [0,1,1,1,1,0]

```

Example 2:**

```

**Input:** seq = "()(())()"
**Output:** [0,0,0,1,1,0,1,1]

```

 

**Constraints:**

	- `1 <= seq.size <= 10000`

## 🧠 Solution Explanation

**Intuition**
The solution works by maintaining two counters, `A` and `B`, which represent the nesting depth of two disjoint subsequences `A` and `B` of the input string `seq`. By iterating through `seq` and updating `A` and `B` accordingly, we can split `seq` into two valid VPS's with maximum nesting depth.

**Approach**
1. Initialize two counters `A` and `B` to 0, and a result list `res` of the same length as `seq`, filled with 0's.
2. Iterate through `seq` from left to right.
3. For each character `c` in `seq`:
   - If `c` is `(`, increment `A` if `A` is less than or equal to `B`, otherwise increment `B`. Set the corresponding element in `res` to 0.
   - If `c` is `)`, decrement `A` if `A` is greater than or equal to `B`, otherwise decrement `B`. Set the corresponding element in `res` to 1.
4. Return the `res` list.

**Time Complexity**
O(n), where n is the length of `seq`. This is because we iterate through `seq` once.

**Space Complexity**
O(n), where n is the length of `seq`. This is because we create a result list of the same length as `seq`.

**Key Insight**
The key insight is that by maintaining two counters `A` and `B`, we can effectively split the input string `seq` into two valid VPS's with maximum nesting depth. This is achieved by carefully updating `A` and `B` based on whether we encounter an opening or closing parenthesis, and using the result list to store the final split.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2025-02-02 |
| 💻 Language | Python |