> 📌 **Cross-listed:** Primary location is [Hash Table/0451-Sort-Characters-By-Frequency](../../Hash-Table/0451-Sort-Characters-By-Frequency). This problem also appears under: **Hash Table**, **String**, **Sorting**, **Heap (Priority Queue)**, **Bucket Sort**, **Counting**

# 451. Sort Characters By Frequency


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sort-characters-by-frequency/)


## 📝 Problem Description

Given a string `s`, sort it in **decreasing order** based on the **frequency** of the characters. The **frequency** of a character is the number of times it appears in the string.

Return *the sorted string*. If there are multiple answers, return *any of them*.

 

Example 1:**

```

**Input:** s = "tree"
**Output:** "eert"
**Explanation:** 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

```

Example 2:**

```

**Input:** s = "cccaaa"
**Output:** "aaaccc"
**Explanation:** Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

```

Example 3:**

```

**Input:** s = "Aabb"
**Output:** "bbAa"
**Explanation:** "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

```

 

**Constraints:**

	- `1 <= s.length <= 5 * 10^5`

	- `s` consists of uppercase and lowercase English letters and digits.

## 🧠 Solution Explanation

**Intuition**
The solution uses a priority queue (heap) to efficiently sort characters by their frequency in the string. By storing the negative frequency of each character, we can use the heap's built-in min-heap property to simulate a max-heap, where characters with higher frequencies are popped first.

**Approach**
1. Create a counter `h1` to count the frequency of each character in the string `s`.
2. Initialize an empty heap `heap`.
3. Iterate over the key-value pairs in the counter `h1`. For each pair, push the negative frequency `(-val)` and the character `key` onto the heap.
4. Initialize an empty string `res`.
5. While the heap is not empty, pop the top element (character and its frequency) from the heap.
6. Append the character to the string `res` as many times as its frequency (i.e., `key * (-val)`).
7. Return the sorted string `res`.

**Time Complexity**
O(n log n), where n is the length of the string `s`. This is because we iterate over the string once to create the counter, and then we push and pop elements from the heap, which takes O(log n) time per operation.

**Space Complexity**
O(n), where n is the length of the string `s`. This is because we need to store the frequency of each character in the counter, and also store the characters and their frequencies in the heap.

**Key Insight**
The key insight is that by storing the negative frequency of each character in the heap, we can use the heap's built-in min-heap property to simulate a max-heap, where characters with higher frequencies are popped first. This allows us to efficiently sort the characters by their frequency in decreasing order.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 97.06%) |
| 💾 Memory | 18.9 MB (Beats 100%) |
| 📅 Solved | 2025-07-06 |
| 💻 Language | Python |