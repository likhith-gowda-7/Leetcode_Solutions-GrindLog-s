> 📌 **Cross-listed:** Primary location is [Array/2109-Adding-Spaces-to-a-String](../../Array/2109-Adding-Spaces-to-a-String). This problem also appears under: **Array**, **Two Pointers**, **String**, **Simulation**

# 2109. Adding Spaces to a String


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/adding-spaces-to-a-string/)


## 📝 Problem Description

You are given a **0-indexed** string `s` and a **0-indexed** integer array `spaces` that describes the indices in the original string where spaces will be added. Each space should be inserted **before** the character at the given index.

	- For example, given `s = "EnjoyYourCoffee"` and `spaces = [5, 9]`, we place spaces before `'Y'` and `'C'`, which are at indices `5` and `9` respectively. Thus, we obtain `"Enjoy **Y**our **C**offee"`.

Return** ***the modified string **after** the spaces have been added.*

 

Example 1:**

```

**Input:** s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
**Output:** "Leetcode Helps Me Learn"
**Explanation:** 
The indices 8, 13, and 15 correspond to the underlined characters in "Leetcode**H**elps**M**e**L**earn".
We then place spaces before those characters.

```

Example 2:**

```

**Input:** s = "icodeinpython", spaces = [1,5,7,9]
**Output:** "i code in py thon"
**Explanation:**
The indices 1, 5, 7, and 9 correspond to the underlined characters in "i**c**ode**i**n**p**y**t**hon".
We then place spaces before those characters.

```

Example 3:**

```

**Input:** s = "spacing", spaces = [0,1,2,3,4,5,6]
**Output:** " s p a c i n g"
**Explanation:**
We are also able to place spaces before the first character of the string.

```

 

**Constraints:**

	- `1 <= s.length <= 3 * 10^5`

	- `s` consists only of lowercase and uppercase English letters.

	- `1 <= spaces.length <= 3 * 10^5`

	- `0 <= spaces[i] <= s.length - 1`

	- All the values of `spaces` are **strictly increasing**.

## 🧠 Solution Explanation

**Intuition**
The solution uses a two-pointer approach to simulate the insertion of spaces at the given indices. It iterates over the `spaces` array, appending substrings of the original string along with spaces to the result list. This approach leverages the fact that strings in Python are immutable, allowing us to build the modified string incrementally.

**Approach**
1. Initialize two pointers: `curr` to keep track of the current position in the string and `res` as an empty list to store the modified string.
2. Iterate over the `spaces` array. For each space index `sp`:
   1. Append the substring from the current position `curr` to the space index `sp` to the result list `res`.
   2. Append a space to the result list `res`.
   3. Update the current position `curr` to the space index `sp`.
3. After iterating over all space indices, append the remaining substring from the current position `curr` to the end of the string to the result list `res`.
4. Join the result list `res` into a single string using the `"".join()` method.

**Time Complexity**
O(n + m), where n is the length of the string `s` and m is the number of space indices. This is because we iterate over the string once and the space indices once.

**Space Complexity**
O(n + m), where n is the length of the string `s` and m is the number of space indices. This is because we store the modified string in the result list, which can grow up to the length of the original string plus the number of space indices.

**Key Insight**
The key insight is to use a two-pointer approach to simulate the insertion of spaces, leveraging the immutability of strings in Python to build the modified string incrementally. This approach avoids the need to create a new string with the spaces inserted, resulting in a more efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 41 ms (Beats 89.77%) |
| 💾 Memory | 48.9 MB (Beats 34.66%) |
| 📅 Solved | 2024-12-16 |
| 💻 Language | Python |