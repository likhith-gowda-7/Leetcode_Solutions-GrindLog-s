# 2075. Decode the Slanted Ciphertext


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/decode-the-slanted-ciphertext/)


## 📝 Problem Description

A string `originalText` is encoded using a **slanted transposition cipher** to a string `encodedText` with the help of a matrix having a **fixed number of rows** `rows`.

`originalText` is placed first in a top-left to bottom-right manner.

![](https://assets.leetcode.com/uploads/2021/11/07/exa11.png)
The blue cells are filled first, followed by the red cells, then the yellow cells, and so on, until we reach the end of `originalText`. The arrow indicates the order in which the cells are filled. All empty cells are filled with `' '`. The number of columns is chosen such that the rightmost column will **not be empty** after filling in `originalText`.

`encodedText` is then formed by appending all characters of the matrix in a row-wise fashion.

![](https://assets.leetcode.com/uploads/2021/11/07/exa12.png)
The characters in the blue cells are appended first to `encodedText`, then the red cells, and so on, and finally the yellow cells. The arrow indicates the order in which the cells are accessed.

For example, if `originalText = "cipher"` and `rows = 3`, then we encode it in the following manner:

![](https://assets.leetcode.com/uploads/2021/10/25/desc2.png)
The blue arrows depict how `originalText` is placed in the matrix, and the red arrows denote the order in which `encodedText` is formed. In the above example, `encodedText = "ch ie pr"`.

Given the encoded string `encodedText` and number of rows `rows`, return *the original string* `originalText`.

**Note:** `originalText` **does not** have any trailing spaces `' '`. The test cases are generated such that there is only one possible `originalText`.

 

Example 1:**

```

**Input:** encodedText = "ch   ie   pr", rows = 3
**Output:** "cipher"
**Explanation:** This is the same example described in the problem description.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/10/26/exam1.png)
```

**Input:** encodedText = "iveo    eed   l te   olc", rows = 4
**Output:** "i love leetcode"
**Explanation:** The figure above denotes the matrix that was used to encode originalText. 
The blue arrows show how we can find originalText from encodedText.

```

Example 3:**

![](https://assets.leetcode.com/uploads/2021/10/26/eg2.png)
```

**Input:** encodedText = "coding", rows = 1
**Output:** "coding"
**Explanation:** Since there is only 1 row, both originalText and encodedText are the same.

```

 

**Constraints:**

	- `0 <= encodedText.length <= 10^6`

	- `encodedText` consists of lowercase English letters and `' '` only.

	- `encodedText` is a valid encoding of some `originalText` that **does not** have trailing spaces.

	- `1 <= rows <= 1000`

	- The testcases are generated such that there is **only one** possible `originalText`.

## 🧠 Solution Explanation

**Intuition**
The solution works by first reconstructing the original matrix used for encoding the text. Then, it reads the matrix in a column-wise manner to obtain the decoded text. This approach is possible because the matrix is filled in a specific order, allowing us to determine the original text by reading the matrix in a different order.

**Approach**
1. Calculate the number of columns in the matrix (`cols`) based on the total length of the encoded text and the number of rows.
2. Initialize an empty matrix with the specified number of rows and columns.
3. Fill the matrix with characters from the encoded text, following the slanted transposition cipher pattern.
4. Read the matrix in a column-wise manner, appending characters to a result list.
5. Remove trailing spaces from the result list.
6. Join the characters in the result list to form the decoded text.

**Time Complexity**
O(n), where n is the length of the encoded text. This is because we are iterating over the encoded text once to fill the matrix and once to read the matrix in a column-wise manner.

**Space Complexity**
O(n), where n is the length of the encoded text. This is because we are storing the encoded text in the matrix and the result list.

**Key Insight**
The key insight is that the matrix is filled in a specific order, allowing us to determine the original text by reading the matrix in a different order. This is made possible by the fact that the rightmost column is not empty after filling in the original text.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 407 ms (Beats 9.08%) |
| 💾 Memory | 39.2 MB (Beats 16.45%) |
| 📅 Solved | 2026-04-04 |
| 💻 Language | Python |