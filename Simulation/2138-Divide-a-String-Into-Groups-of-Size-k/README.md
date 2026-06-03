> 📌 **Cross-listed:** Primary location is [String/2138-Divide-a-String-Into-Groups-of-Size-k](../../String/2138-Divide-a-String-Into-Groups-of-Size-k). This problem also appears under: **String**, **Simulation**

# 2138. Divide a String Into Groups of Size k


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/)


## 📝 Problem Description

A string `s` can be partitioned into groups of size `k` using the following procedure:

	- The first group consists of the first `k` characters of the string, the second group consists of the next `k` characters of the string, and so on. Each element can be a part of **exactly one** group.

	- For the last group, if the string **does not** have `k` characters remaining, a character `fill` is used to complete the group.

Note that the partition is done so that after removing the `fill` character from the last group (if it exists) and concatenating all the groups in order, the resultant string should be `s`.

Given the string `s`, the size of each group `k` and the character `fill`, return *a string array denoting the **composition of every group** *`s`* has been divided into, using the above procedure*.

 

Example 1:**

```

**Input:** s = "abcdefghi", k = 3, fill = "x"
**Output:** ["abc","def","ghi"]
**Explanation:**
The first 3 characters "abc" form the first group.
The next 3 characters "def" form the second group.
The last 3 characters "ghi" form the third group.
Since all groups can be completely filled by characters from the string, we do not need to use fill.
Thus, the groups formed are "abc", "def", and "ghi".

```

Example 2:**

```

**Input:** s = "abcdefghij", k = 3, fill = "x"
**Output:** ["abc","def","ghi","jxx"]
**Explanation:**
Similar to the previous example, we are forming the first three groups "abc", "def", and "ghi".
For the last group, we can only use the character 'j' from the string. To complete this group, we add 'x' twice.
Thus, the 4 groups formed are "abc", "def", "ghi", and "jxx".

```

 

**Constraints:**

	- `1 <= s.length <= 100`

	- `s` consists of lowercase English letters only.

	- `1 <= k <= 100`

	- `fill` is a lowercase English letter.

## 🧠 Solution Explanation

**Intuition**
This solution works by iterating over the input string `s` and grouping its characters into chunks of size `k`. If the string does not have `k` characters remaining, it uses the `fill` character to complete the last group. The solution returns an array of strings, where each string represents a group in the partitioned string.

**Approach**
1. Initialize an empty list `res` to store the groups and a counter `c` to keep track of the current group size.
2. Initialize an empty string `val` to build the current group.
3. Iterate over each character `ch` in the input string `s`.
4. Increment the counter `c` and append the character `ch` to the current group `val`.
5. If the counter `c` reaches `k`, append the current group `val` to the result list `res`, reset the counter `c` and the current group `val`.
6. After iterating over the entire string, if there are remaining characters, use the `fill` character to complete the last group and append it to the result list `res`.

**Time Complexity**
O(n), where n is the length of the input string `s`. This is because we iterate over each character in the string once.

**Space Complexity**
O(n), where n is the length of the input string `s`. This is because we store the partitioned groups in the result list `res`, which can have up to n/k elements.

**Key Insight**
The key insight here is to use a counter `c` to keep track of the current group size and a string `val` to build the current group. This allows us to efficiently partition the string into groups of size `k` and handle the case where the string does not have `k` characters remaining.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-06-22 |
| 💻 Language | Python |