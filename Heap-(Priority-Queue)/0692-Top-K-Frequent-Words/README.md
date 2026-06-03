> 📌 **Cross-listed:** Primary location is [Array/0692-Top-K-Frequent-Words](../../Array/0692-Top-K-Frequent-Words). This problem also appears under: **Array**, **Hash Table**, **String**, **Trie**, **Sorting**, **Heap (Priority Queue)**, **Bucket Sort**, **Counting**

# 692. Top K Frequent Words


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Trie](https://img.shields.io/badge/Trie-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/top-k-frequent-words/)


## 📝 Problem Description

Given an array of strings `words` and an integer `k`, return *the *`k`* most frequent strings*.

Return the answer **sorted** by **the frequency** from highest to lowest. Sort the words with the same frequency by their **lexicographical order**.

 

Example 1:**

```

**Input:** words = ["i","love","leetcode","i","love","coding"], k = 2
**Output:** ["i","love"]
**Explanation:** "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

```

Example 2:**

```

**Input:** words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
**Output:** ["the","is","sunny","day"]
**Explanation:** "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

```

 

**Constraints:**

	- `1 <= words.length <= 500`

	- `1 <= words[i].length <= 10`

	- `words[i]` consists of lowercase English letters.

	- `k` is in the range `[1, The number of **unique** words[i]]`

 

**Follow-up:** Could you solve it in `O(n log(k))` time and `O(n)` extra space?

## 🧠 Solution Explanation

**Intuition**
The solution uses a combination of a hash map (Counter) to count the frequency of each word, and a frequency array to store the words with the same frequency. By sorting the hash map and iterating through the frequency array in reverse order, we can efficiently find the k most frequent words.

**Approach**
1. Use a hash map (Counter) to count the frequency of each word in the input array.
2. Sort the hash map by value (frequency) and then by key (word).
3. Create a frequency array with the maximum frequency as the size.
4. Iterate through the sorted hash map and append each word to the corresponding frequency array.
5. Iterate through the frequency array in reverse order, appending each word to the result array until we have k words.

**Time Complexity**
O(n log n) due to the sorting of the hash map, where n is the number of unique words.

**Space Complexity**
O(n) for the hash map and frequency array, where n is the number of unique words.

**Key Insight**
The key insight is to use a frequency array to store the words with the same frequency, allowing us to efficiently iterate through the words in reverse order of frequency and lexicographical order. This approach avoids the need for a complex sorting algorithm and makes the solution more efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2025-06-18 |
| 💻 Language | Python |