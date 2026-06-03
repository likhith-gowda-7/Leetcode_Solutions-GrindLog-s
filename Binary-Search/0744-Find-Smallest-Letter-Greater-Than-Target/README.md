> 📌 **Cross-listed:** Primary location is [Array/0744-Find-Smallest-Letter-Greater-Than-Target](../../Array/0744-Find-Smallest-Letter-Greater-Than-Target). This problem also appears under: **Array**, **Binary Search**

# 744. Find Smallest Letter Greater Than Target


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)


## 📝 Problem Description

You are given an array of characters `letters` that is sorted in **non-decreasing order**, and a character `target`. There are **at least two different** characters in `letters`.

Return *the smallest character in *`letters`* that is lexicographically greater than *`target`. If such a character does not exist, return the first character in `letters`.

 

Example 1:**

```

**Input:** letters = ["c","f","j"], target = "a"
**Output:** "c"
**Explanation:** The smallest character that is lexicographically greater than 'a' in letters is 'c'.

```

Example 2:**

```

**Input:** letters = ["c","f","j"], target = "c"
**Output:** "f"
**Explanation:** The smallest character that is lexicographically greater than 'c' in letters is 'f'.

```

Example 3:**

```

**Input:** letters = ["x","x","y","y"], target = "z"
**Output:** "x"
**Explanation:** There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

```

 

**Constraints:**

	- `2 <= letters.length <= 10^4`

	- `letters[i]` is a lowercase English letter.

	- `letters` is sorted in **non-decreasing** order.

	- `letters` contains at least two different characters.

	- `target` is a lowercase English letter.

## 🧠 Solution Explanation

**Intuition**
The solution utilizes a modified binary search approach to efficiently find the smallest character in the sorted array that is lexicographically greater than the target character. This approach is possible because the array is sorted in non-decreasing order, allowing us to take advantage of the property that if an element is greater than the target, all elements to its left are also greater.

**Approach**
1. Initialize two pointers, `l` and `r`, to the start and end of the array, respectively.
2. Perform a binary search by calculating the midpoint `mid` of the current search range `[l, r]`.
3. Compare the character at the midpoint `letters[mid]` with the target character. If it's greater, update the right pointer `r` to `mid - 1`. Otherwise, update the left pointer `l` to `mid + 1`.
4. Repeat steps 2-3 until `l` is greater than `r`.
5. If `l` is within the valid range, return the character at index `l`. Otherwise, return the first character in the array.

**Time Complexity**
O(log n), where n is the length of the array. This is because we're performing a binary search, which reduces the search space by half at each step.

**Space Complexity**
O(1), as we're only using a constant amount of space to store the pointers and the midpoint.

**Key Insight**
The key insight here is that we can take advantage of the sorted property of the array to perform a modified binary search. By comparing the midpoint character with the target, we can effectively eliminate half of the search space at each step, leading to a logarithmic time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 20.9 MB (Beats 15.83%) |
| 📅 Solved | 2026-01-31 |
| 💻 Language | Python |