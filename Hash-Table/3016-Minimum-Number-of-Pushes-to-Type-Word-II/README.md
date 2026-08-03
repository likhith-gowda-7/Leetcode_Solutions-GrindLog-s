# 3016. Minimum Number of Pushes to Type Word II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/)


## 📝 Problem Description

You are given a string `word` containing lowercase English letters.

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

![](https://assets.leetcode.com/uploads/2024/08/20/edited.png)
```

**Input:** word = "xyzxyzxyzxyz"
**Output:** 12
**Explanation:** The remapped keypad given in the image provides the minimum cost.
"x" -> one push on key 2
"y" -> one push on key 3
"z" -> one push on key 4
Total cost is 1 * 4 + 1 * 4 + 1 * 4 = 12
It can be shown that no other mapping can provide a lower cost.
Note that the key 9 is not mapped to any letter: it is not necessary to map letters to every key, but to map all the letters.

```

Example 3:**

![](https://assets.leetcode.com/uploads/2023/12/27/keypadv2.png)
```

**Input:** word = "aabbccddeeffgghhiiiiii"
**Output:** 24
**Explanation:** The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
"f" -> one push on key 7
"g" -> one push on key 8
"h" -> two pushes on key 9
"i" -> one push on key 9
Total cost is 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 2 * 2 + 6 * 1 = 24.
It can be shown that no other mapping can provide a lower cost.

```

 

**Constraints:**

	- `1 <= word.length <= 10^5`

	- `word` consists of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution takes advantage of the fact that the keys on a telephone keypad are arranged in a way that allows for efficient mapping of letters to keys. By remapping the keys to distinct collections of letters, we can minimize the number of pushes needed to type the string `word`. The key insight is to sort the counts of each letter in descending order and then assign the keys to the most frequent letters first.

**Approach**
1. Count the frequency of each letter in the string `word` and store it in the `counts` list.
2. Sort the `counts` list in descending order.
3. Initialize the result `res` to 0.
4. Iterate through the sorted `counts` list. For each count, calculate the number of pushes needed by multiplying the count by the minimum number of keys required to type that many letters. The minimum number of keys is calculated as `((idx//8)+1)`, where `idx` is the index of the count in the sorted list.
5. Add the calculated pushes to the result `res`.
6. Return the final result `res`.

**Time Complexity**
O(n log n), where n is the number of unique letters in the string `word`. This is because we are sorting the `counts` list, which takes O(n log n) time.

**Space Complexity**
O(n), where n is the number of unique letters in the string `word`. This is because we are storing the frequency of each letter in the `counts` list.

**Key Insight**
The key insight is to assign the keys to the most frequent letters first, which allows us to minimize the number of pushes needed to type the string `word`. This is achieved by sorting the `counts` list in descending order and then calculating the minimum number of keys required to type each letter.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 12 ms (Beats 99.52%) |
| 💾 Memory | 19.8 MB (Beats 91.15%) |
| 📅 Solved | 2026-07-31 |
| 💻 Language | Python |