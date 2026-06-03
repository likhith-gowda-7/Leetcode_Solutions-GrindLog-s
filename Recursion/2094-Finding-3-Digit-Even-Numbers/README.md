> 📌 **Cross-listed:** Primary location is [Array/2094-Finding-3-Digit-Even-Numbers](../../Array/2094-Finding-3-Digit-Even-Numbers). This problem also appears under: **Array**, **Hash Table**, **Recursion**, **Sorting**, **Enumeration**

# 2094. Finding 3-Digit Even Numbers


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Recursion](https://img.shields.io/badge/Recursion-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/finding-3-digit-even-numbers/)


## 📝 Problem Description

You are given an integer array `digits`, where each element is a digit. The array may contain duplicates.

You need to find **all** the **unique** integers that follow the given requirements:

	- The integer consists of the **concatenation** of **three** elements from `digits` in **any** arbitrary order.

	- The integer does not have **leading zeros**.

	- The integer is **even**.

For example, if the given `digits` were `[1, 2, 3]`, integers `132` and `312` follow the requirements.

Return *a **sorted** array of the unique integers.*

 

Example 1:**

```

**Input:** digits = [2,1,3,0]
**Output:** [102,120,130,132,210,230,302,310,312,320]
**Explanation:** All the possible integers that follow the requirements are in the output array. 
Notice that there are no **odd** integers or integers with **leading zeros**.

```

Example 2:**

```

**Input:** digits = [2,2,8,8,2]
**Output:** [222,228,282,288,822,828,882]
**Explanation:** The same digit can be used as many times as it appears in digits. 
In this example, the digit 8 is used twice each time in 288, 828, and 882. 

```

Example 3:**

```

**Input:** digits = [3,7,5]
**Output:** []
**Explanation:** No **even** integers can be formed using the given digits.

```

 

**Constraints:**

	- `3 <= digits.length <= 100`

	- `0 <= digits[i] <= 9`

## 🧠 Solution Explanation

**Intuition**
The solution uses a hash table to count the frequency of each digit in the input array. It then iterates over all possible combinations of three digits, ensuring that the resulting integer is even and does not have leading zeros. The unique integers are stored in a result list, which is returned at the end.

**Approach**
1. Create a hash table `h1` to count the frequency of each digit in the input array `digits`.
2. Initialize an empty list `res` to store the unique integers that meet the requirements.
3. Iterate over all possible hundreds digits `i` from 1 to 9.
4. For each hundreds digit `i`, create a copy of the hash table `check` and decrement its count for the hundreds digit.
5. Iterate over all possible tens digits `j` from 0 to 9.
6. For each tens digit `j`, create a copy of the hash table `check` and decrement its count for the tens digit.
7. Iterate over all possible units digits `k` from 0 to 9, incrementing by 2 to ensure the integer is even.
8. For each units digit `k`, check if the count in the hash table `check` is greater than 0. If it is, append the integer formed by concatenating the hundreds, tens, and units digits to the result list `res`.
9. Increment the count for the tens digit `j` in the hash table `check` to backtrack and try other combinations.
10. Return the sorted result list `res`.

**Time Complexity**
O(9 * 10 * 5) = O(450), where 9 is the number of possible hundreds digits, 10 is the number of possible tens digits, and 5 is the number of possible units digits (since we only consider even units digits).

**Space Complexity**
O(10) for the hash table `h1` and O(9 * 10 * 5) = O(450) for the result list `res`, which is dominated by the time complexity.

**Key Insight**
The key insight is to use a hash table to count the frequency of each digit and then iterate over all possible combinations of three digits, ensuring that the resulting integer meets the requirements. This approach avoids generating all possible integers and then filtering them, which would be more efficient but also more complex.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 98.57%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-05-13 |
| 💻 Language | Python |