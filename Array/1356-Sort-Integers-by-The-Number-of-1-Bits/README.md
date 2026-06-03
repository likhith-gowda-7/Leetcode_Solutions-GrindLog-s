# 1356. Sort Integers by The Number of 1 Bits


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/)


## 📝 Problem Description

You are given an integer array `arr`. Sort the integers in the array in ascending order by the number of `1`'s in their binary representation and in case of two or more integers have the same number of `1`'s you have to sort them in ascending order.

Return *the array after sorting it*.

 

Example 1:**

```

**Input:** arr = [0,1,2,3,4,5,6,7,8]
**Output:** [0,1,2,4,8,3,5,6,7]
**Explantion:** [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]

```

Example 2:**

```

**Input:** arr = [1024,512,256,128,64,32,16,8,4,2,1]
**Output:** [1,2,4,8,16,32,64,128,256,512,1024]
**Explantion:** All integers have 1 bit in the binary representation, you should just sort them in ascending order.

```

 

**Constraints:**

	- `1 <= arr.length <= 500`

	- `0 <= arr[i] <= 10^4`

## 🧠 Solution Explanation

**Intuition**
The solution works by leveraging Python's built-in sorting functionality. We use a custom sorting key that takes into account the number of 1 bits in the binary representation of each integer. This key is a tuple where the first element is the count of 1 bits and the second element is the integer itself. This allows the sorting algorithm to first sort by the number of 1 bits and then by the integer value in case of a tie.

**Approach**
1. Use Python's built-in `sort` method to sort the input array `arr`.
2. Define a custom sorting key using a lambda function.
3. In the lambda function, convert the integer to binary using `bin(x)`.
4. Count the number of 1 bits in the binary representation using the `count` method.
5. Return a tuple where the first element is the count of 1 bits and the second element is the integer itself.
6. The `sort` method will first sort by the first element of the tuple (count of 1 bits) and then by the second element (integer value) in case of a tie.

**Time Complexity**
The time complexity of this solution is O(n log n), where n is the length of the input array. This is because the `sort` method has a time complexity of O(n log n) in the worst case.

**Space Complexity**
The space complexity of this solution is O(n), where n is the length of the input array. This is because the `sort` method needs to create a new array to store the sorted elements.

**Key Insight**
The key insight here is that Python's built-in sorting algorithm is stable, meaning that when multiple records have the same key, their original order is preserved. By using a tuple as the sorting key, we can take advantage of this stability to first sort by the number of 1 bits and then by the integer value in case of a tie. This makes the solution efficient and easy to understand.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 4 ms (Beats 62.38%) |
| 💾 Memory | 19.6 MB (Beats 7.82%) |
| 📅 Solved | 2026-02-25 |
| 💻 Language | Python |