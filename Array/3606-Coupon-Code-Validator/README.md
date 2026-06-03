# 3606. Coupon Code Validator


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/coupon-code-validator/)


## 📝 Problem Description

You are given three arrays of length `n` that describe the properties of `n` coupons: `code`, `businessLine`, and `isActive`. The `i^th `coupon has:

	- `code[i]`: a **string** representing the coupon identifier.

	- `businessLine[i]`: a **string** denoting the business category of the coupon.

	- `isActive[i]`: a **boolean** indicating whether the coupon is currently active.

A coupon is considered **valid** if all of the following conditions hold:

	- `code[i]` is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (`_`).

	- `businessLine[i]` is one of the following four categories: `"electronics"`, `"grocery"`, `"pharmacy"`, `"restaurant"`.

	- `isActive[i]` is **true**.

Return an array of the **codes** of all valid coupons, **sorted** first by their **businessLine** in the order: `"electronics"`, `"grocery"`, `"pharmacy", "restaurant"`, and then by **code** in lexicographical (ascending) order within each category.

 

Example 1:**

**Input:** code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true]

**Output:** ["PHARMA5","SAVE20"]

**Explanation:**

	- First coupon is valid.

	- Second coupon has empty code (invalid).

	- Third coupon is valid.

	- Fourth coupon has special character `@` (invalid).

Example 2:**

**Input:** code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [false,true,true]

**Output:** ["ELECTRONICS_50"]

**Explanation:**

	- First coupon is inactive (invalid).

	- Second coupon is valid.

	- Third coupon has invalid business line (invalid).

 

**Constraints:**

	- `n == code.length == businessLine.length == isActive.length`

	- `1 <= n <= 100`

	- `0 <= code[i].length, businessLine[i].length <= 100`

	- `code[i]` and `businessLine[i]` consist of printable ASCII characters.

	- `isActive[i]` is either `true` or `false`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a hash table to group coupons by business category and then filters out invalid coupons. It leverages a helper function to check the validity of each coupon's code.

**Approach**
1. Initialize a hash table `fields` with four keys representing the business categories and empty lists as values.
2. Define a helper function `check(s)` to verify if a string `s` consists only of alphanumeric characters and underscores.
3. Iterate through the input arrays `code`, `businessLine`, and `isActive` simultaneously using their indices.
4. For each coupon, check if it's valid by verifying the following conditions:
	* The coupon code is non-empty.
	* The business category is one of the four allowed categories.
	* The coupon is active.
5. If the coupon is valid, add its code to the corresponding list in the `fields` hash table.
6. After processing all coupons, iterate through the `fields` hash table and extract the valid coupon codes from the non-empty lists.
7. Sort the valid coupon codes for each business category and concatenate them into a single list.

**Time Complexity**
O(n), where n is the number of coupons, since we iterate through the input arrays once and perform constant-time operations for each coupon.

**Space Complexity**
O(n), as in the worst case, we might need to store all coupon codes in the `fields` hash table.

**Key Insight**
The key insight is to use a hash table to group coupons by business category, which allows us to efficiently filter out invalid coupons and extract the valid ones. This approach avoids the need for multiple iterations and conditional checks, making it more efficient than a naive solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 73.99%) |
| 💾 Memory | 18.2 MB (Beats 100%) |
| 📅 Solved | 2025-12-13 |
| 💻 Language | Python |