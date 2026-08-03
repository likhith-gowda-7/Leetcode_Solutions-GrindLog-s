> 📌 **Cross-listed:** Primary location is [Math/3014-Minimum-Number-of-Pushes-to-Type-Word-I](../../Math/3014-Minimum-Number-of-Pushes-to-Type-Word-I). This problem also appears under: **Math**, **String**, **Greedy**

# 3014. Minimum Number of Pushes to Type Word I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![String](https://img.shields.io/badge/String-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/)


## 📝 Problem Description

You are given a string `word` containing **distinct** lowercase English letters.

Telephone keypads have keys mapped with **distinct** collections of lowercase English letters, which can be used to form words by pushing them. For example, the key `2` is mapped with `["a","b","c"]`, we need to push the key one time to type `"a"`, two times to type `"b"`, and three times to type `"c"` *.*

It is allowed to remap the keys numbered `2` to `9` to **distinct** collections of letters. The keys can be remapped to **any** amount of letters, but each letter **must** be mapped to **exactly** one key. You need to find the **minimum** number of times the keys will be pushed to type the string `word`.

Return *the **minimum** number of pushes needed to type *`word` *after remapping the keys*.

An example mapping of letters to keys on a telephone keypad is given below. Note that `1`, `*`, `#`, and `0` do **not** map to any letters.

![](https://assets.leetcode.com/uploads/2023/12/26/keypaddesc.png)
 

Example 1:**

![](https://assets.leetcode.com/uploads/2023/12/26/keypadv1e1.png)
```

**Input:** word = "abcde"
**Output:** 5
**Explanation:** The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
Total cost is 1 + 1 + 1 + 1 + 1 = 5.
It can be shown that no other mapping can provide a lower cost.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2023/12/26/keypadv1e2.png)
```

**Input:** word = "xycdefghij"
**Output:** 12
**Explanation:** The remapped keypad given in the image provides the minimum cost.
"x" -> one push on key 2
"y" -> two pushes on key 2
"c" -> one push on key 3
"d" -> two pushes on key 3
"e" -> one push on key 4
"f" -> one push on key 5
"g" -> one push on key 6
"h" -> one push on key 7
"i" -> one push on key 8
"j" -> one push on key 9
Total cost is 1 + 2 + 1 + 2 + 1 + 1 + 1 + 1 + 1 + 1 = 12.
It can be shown that no other mapping can provide a lower cost.

```

 

**Constraints:**

	- `1 <= word.length <= 26`

	- `word` consists of lowercase English letters.

	- All letters in `word` are distinct.

## 🧠 Solution Explanation

**Intuition**
The solution uses a greedy approach to minimize the number of key presses required to type the given word. It assigns the first 8 characters to the first key press, the next 8 characters to the second key press, and so on, until all characters are typed.

**Approach**
1. Initialize the result variable `res` to 0 and the number of key presses `presses` to 1.
2. While the length of the word `n` is greater than or equal to 8, calculate the number of key presses required to type the next 8 characters and add it to the result.
3. Increment the number of key presses `presses` by 1 and subtract 8 from the length of the word `n`.
4. Once the length of the word `n` is less than 8, calculate the number of key presses required to type the remaining characters and add it to the result.
5. Return the total result.

**Time Complexity**
O(n), where n is the length of the word. This is because we iterate over the word at most twice: once to calculate the number of key presses for the first 8 characters, and once to calculate the number of key presses for the remaining characters.

**Space Complexity**
O(1), as we only use a constant amount of space to store the result and the number of key presses.

**Key Insight**
The key insight is to use a greedy approach to assign characters to key presses, always trying to type the maximum number of characters with the minimum number of key presses. This approach ensures that we minimize the total number of key presses required to type the word.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 53.64%) |
| 📅 Solved | 2026-07-30 |
| 💻 Language | Python |