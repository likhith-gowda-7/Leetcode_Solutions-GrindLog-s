> 📌 **Cross-listed:** Primary location is [Array/1233-Remove-Sub-Folders-from-the-Filesystem](../../Array/1233-Remove-Sub-Folders-from-the-Filesystem). This problem also appears under: **Array**, **String**, **Depth-First Search**, **Trie**

# 1233. Remove Sub-Folders from the Filesystem


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Trie](https://img.shields.io/badge/Trie-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/)


## 📝 Problem Description

Given a list of folders `folder`, return *the folders after removing all **sub-folders** in those folders*. You may return the answer in **any order**.

If a `folder[i]` is located within another `folder[j]`, it is called a **sub-folder** of it. A sub-folder of `folder[j]` must start with `folder[j]`, followed by a `"/"`. For example, `"/a/b"` is a sub-folder of `"/a"`, but `"/b"` is not a sub-folder of `"/a/b/c"`.

The format of a path is one or more concatenated strings of the form: `'/'` followed by one or more lowercase English letters.

	- For example, `"/leetcode"` and `"/leetcode/problems"` are valid paths while an empty string and `"/"` are not.

 

Example 1:**

```

**Input:** folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
**Output:** ["/a","/c/d","/c/f"]
**Explanation:** Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.

```

Example 2:**

```

**Input:** folder = ["/a","/a/b/c","/a/b/d"]
**Output:** ["/a"]
**Explanation:** Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".

```

Example 3:**

```

**Input:** folder = ["/a/b/c","/a/b/ca","/a/b/d"]
**Output:** ["/a/b/c","/a/b/ca","/a/b/d"]

```

 

**Constraints:**

	- `1 <= folder.length <= 4 * 10^4`

	- `2 <= folder[i].length <= 100`

	- `folder[i]` contains only lowercase letters and `'/'`.

	- `folder[i]` always starts with the character `'/'`.

	- Each folder name is **unique**.

## 🧠 Solution Explanation

**Intuition**
The solution takes advantage of the fact that the input list of folders is sorted. By iterating through the sorted list, we can efficiently identify and remove sub-folders by checking if the current folder starts with the last added folder in the result list.

**Approach**
1. Sort the input list of folders in ascending order.
2. Initialize the result list with the first folder in the sorted list.
3. Iterate through the remaining folders in the sorted list.
4. For each folder, check if it starts with the last added folder in the result list (including the trailing "/").
5. If it does not start with the last added folder, add it to the result list.
6. Return the result list.

**Time Complexity**
O(n log n) due to the sorting operation, where n is the number of folders. The subsequent iteration through the sorted list takes O(n) time.

**Space Complexity**
O(n) for storing the result list, where n is the number of folders.

**Key Insight**
The key insight is that by sorting the input list of folders, we can efficiently identify and remove sub-folders by checking if the current folder starts with the last added folder in the result list. This approach takes advantage of the fact that sub-folders are located within their parent folders in a sorted list.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 19 ms (Beats 90.97%) |
| 💾 Memory | 30.4 MB (Beats 100%) |
| 📅 Solved | 2025-07-20 |
| 💻 Language | Python |