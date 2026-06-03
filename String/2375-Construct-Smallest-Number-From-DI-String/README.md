# 2375. Construct Smallest Number From DI String


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/construct-smallest-number-from-di-string/)


## 📝 Problem Description

You are given a **0-indexed** string `pattern` of length `n` consisting of the characters `'I'` meaning **increasing** and `'D'` meaning **decreasing**.

A **0-indexed** string `num` of length `n + 1` is created using the following conditions:

	- `num` consists of the digits `'1'` to `'9'`, where each digit is used **at most** once.

	- If `pattern[i] == 'I'`, then `num[i] < num[i + 1]`.

	- If `pattern[i] == 'D'`, then `num[i] > num[i + 1]`.

Return *the lexicographically **smallest** possible string *`num`* that meets the conditions.*

 

Example 1:**

```

**Input:** pattern = "IIIDIDDD"
**Output:** "123549876"
**Explanation:
**At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.
```

Example 2:**

```

**Input:** pattern = "DDD"
**Output:** "4321"
**Explanation:**
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.

```

 

**Constraints:**

	- `1 <= pattern.length <= 8`

	- `pattern` consists of only the letters `'I'` and `'D'`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a stack to keep track of the digits that can be used to construct the smallest possible string. When encountering an 'I' in the pattern, it pops the largest digit from the stack and appends it to the result, ensuring that the current digit is smaller than the next one. When encountering a 'D' in the pattern, it simply appends the top of the stack to the result, ensuring that the current digit is larger than the next one.

**Approach**
1. Initialize an empty result list and a stack with digits from 1 to n+1.
2. Iterate through the pattern, and for each character:
   - If it's an 'I' or we're at the end of the pattern, pop the largest digit from the stack and append it to the result.
   - If it's a 'D', append the top of the stack to the result.
3. Join the result list into a string and return it.

**Time Complexity**
O(n), where n is the length of the pattern. This is because we make a single pass through the pattern.

**Space Complexity**
O(n), where n is the length of the pattern. This is because in the worst case, we might need to push all digits onto the stack.

**Key Insight**
The key insight is that we can use a stack to efficiently keep track of the digits that can be used to construct the smallest possible string, and that we only need to consider the current digit and the next one when making decisions. This allows us to avoid considering all possible combinations of digits, making the solution much more efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.5 MB (Beats 100%) |
| 📅 Solved | 2025-02-18 |
| 💻 Language | Python |