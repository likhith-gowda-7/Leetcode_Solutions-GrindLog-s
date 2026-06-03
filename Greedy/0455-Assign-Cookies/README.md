> 📌 **Cross-listed:** Primary location is [Array/0455-Assign-Cookies](../../Array/0455-Assign-Cookies). This problem also appears under: **Array**, **Two Pointers**, **Greedy**, **Sorting**

# 455. Assign Cookies


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/assign-cookies/)


## 📝 Problem Description

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child `i` has a greed factor `g[i]`, which is the minimum size of a cookie that the child will be content with; and each cookie `j` has a size `s[j]`. If `s[j] >= g[i]`, we can assign the cookie `j` to the child `i`, and the child `i` will be content. Your goal is to maximize the number of your content children and output the maximum number.

 

Example 1:**

```

**Input:** g = [1,2,3], s = [1,1]
**Output:** 1
**Explanation:** You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

```

Example 2:**

```

**Input:** g = [1,2], s = [1,2,3]
**Output:** 2
**Explanation:** You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.

```

 

**Constraints:**

	- `1 <= g.length <= 3 * 10^4`

	- `0 <= s.length <= 3 * 10^4`

	- `1 <= g[i], s[j] <= 2^31 - 1`

 

**Note:** This question is the same as [ 2410: Maximum Matching of Players With Trainers.](https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/)

## 🧠 Solution Explanation

**Intuition**
The solution works by sorting both the children's greed factors and the cookie sizes, then iterating through the cookies and assigning them to the children with the smallest greed factors that can be satisfied. This greedy approach maximizes the number of content children.

**Approach**
1. If there are no cookies, return 0 as no children can be satisfied.
2. Sort the children's greed factors and cookie sizes in ascending order.
3. Initialize a pointer `i` to 0, which will keep track of the current child being considered.
4. Iterate through the sorted cookie sizes. For each cookie, check if the current child `i` can be satisfied (i.e., the cookie size is greater than or equal to the child's greed factor).
5. If the child can be satisfied, increment the pointer `i` to consider the next child.
6. After iterating through all cookies, return the value of `i`, which represents the maximum number of content children.

**Time Complexity**
O(n log n) due to the sorting of the children's greed factors and cookie sizes, where n is the number of children.

**Space Complexity**
O(1) as the sorting is done in-place and the iteration through the cookies only requires a single pointer.

**Key Insight**
The key insight is that by sorting both the children's greed factors and the cookie sizes, we can efficiently find the maximum number of content children by iterating through the cookies and assigning them to the children with the smallest greed factors that can be satisfied. This greedy approach takes advantage of the fact that the children's greed factors are sorted in ascending order, allowing us to maximize the number of content children.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 11 ms (Beats 97.57%) |
| 💾 Memory | 19.8 MB (Beats 100%) |
| 📅 Solved | 2025-12-03 |
| 💻 Language | Python |