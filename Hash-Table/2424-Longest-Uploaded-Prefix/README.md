# 2424. Longest Uploaded Prefix


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple) ![Design](https://img.shields.io/badge/Design-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-uploaded-prefix/)


## 📝 Problem Description

You are given a stream of `n` videos, each represented by a **distinct** number from `1` to `n` that you need to "upload" to a server. You need to implement a data structure that calculates the length of the **longest uploaded prefix** at various points in the upload process.

We consider `i` to be an uploaded prefix if all videos in the range `1` to `i` (**inclusive**) have been uploaded to the server. The longest uploaded prefix is the **maximum **value of `i` that satisfies this definition.

Implement the `LUPrefix `class:

	- `LUPrefix(int n)` Initializes the object for a stream of `n` videos.

	- `void upload(int video)` Uploads `video` to the server.

	- `int longest()` Returns the length of the **longest uploaded prefix** defined above.

 

Example 1:**

```

**Input**
["LUPrefix", "upload", "longest", "upload", "longest", "upload", "longest"]
[[4], [3], [], [1], [], [2], []]
**Output**
[null, null, 0, null, 1, null, 3]

**Explanation**
LUPrefix server = new LUPrefix(4);   // Initialize a stream of 4 videos.
server.upload(3);                    // Upload video 3.
server.longest();                    // Since video 1 has not been uploaded yet, there is no prefix.
                                     // So, we return 0.
server.upload(1);                    // Upload video 1.
server.longest();                    // The prefix [1] is the longest uploaded prefix, so we return 1.
server.upload(2);                    // Upload video 2.
server.longest();                    // The prefix [1,2,3] is the longest uploaded prefix, so we return 3.

```

 

**Constraints:**

	- `1 <= n <= 10^5`

	- `1 <= video <= n`

	- All values of `video` are **distinct**.

	- At most `2 * 10^5` calls **in total** will be made to `upload` and `longest`.

	- At least one call will be made to `longest`.

## 🧠 Solution Explanation

**Intuition**
The solution utilizes a binary search-like approach to track the longest uploaded prefix by maintaining a counter that increments whenever a video is uploaded and all previous videos are also uploaded. This allows for efficient calculation of the longest uploaded prefix at any point in the upload process.

**Approach**
1. Initialize a boolean array `arr` of size `n` to track whether each video has been uploaded or not. Set all elements to `False`.
2. Initialize a counter `ind_count` to 0, which will keep track of the longest uploaded prefix.
3. In the `upload` method:
   a. Set the corresponding element in `arr` to `True` to indicate that the video has been uploaded.
   b. While `ind_count` is less than `n` and the element at `ind_count` in `arr` is `True`, increment `ind_count`. This effectively moves the counter forward as long as all videos up to `ind_count` have been uploaded.
4. In the `longest` method, return the current value of `ind_count`, which represents the length of the longest uploaded prefix.

**Time Complexity**
O(1) amortized. The `upload` method performs a constant number of operations, and the `longest` method simply returns the current value of `ind_count`, which is also constant. However, the while loop in the `upload` method can potentially execute `n` times in the worst case, but this is amortized over multiple `upload` calls.

**Space Complexity**
O(n) for the boolean array `arr`.

**Key Insight**
The key insight is that we only need to keep track of the longest uploaded prefix, which allows us to use a simple counter to efficiently calculate the longest uploaded prefix at any point in the upload process. This approach avoids the need for explicit binary search or other more complex data structures.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 94 ms (Beats 73.49%) |
| 💾 Memory | 73 MB (Beats 43.37%) |
| 📅 Solved | 2025-07-01 |
| 💻 Language | Python |