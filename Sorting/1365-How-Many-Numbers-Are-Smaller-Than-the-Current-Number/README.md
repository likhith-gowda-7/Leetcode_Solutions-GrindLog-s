> 📌 **Cross-listed:** Primary location is [Array/1365-How-Many-Numbers-Are-Smaller-Than-the-Current-Number](../../Array/1365-How-Many-Numbers-Are-Smaller-Than-the-Current-Number). This problem also appears under: **Array**, **Hash Table**, **Sorting**, **Counting Sort**

# 1365. How Many Numbers Are Smaller Than the Current Number


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Counting Sort](https://img.shields.io/badge/Counting%20Sort-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)


## 📝 Problem Description

Given the array `nums`, for each `nums[i]` find out how many numbers in the array are smaller than it. That is, for each `nums[i]` you have to count the number of valid `j's` such that `j != i` **and** `nums[j] < nums[i]`.

Return the answer in an array.

 

Example 1:**

```

**Input:** nums = [8,1,2,2,3]
**Output:** [4,0,1,1,3]
**Explanation:** 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

```

Example 2:**

```

**Input:** nums = [6,5,4,8]
**Output:** [2,1,0,3]

```

Example 3:**

```

**Input:** nums = [7,7,7,7]
**Output:** [0,0,0,0]

```

 

**Constraints:**

	- `2 <= nums.length <= 500`

	- `0 <= nums[i] <= 100`

## 🧠 Solution Explanation

**Intuition**
This solution works by first creating a hash table to store the indices of each number in the input array. Then, it sorts the array and iterates through it, updating the result array with the count of smaller numbers for each number.

**Approach**
1. Create a hash table `h1` to store the indices of each number in the input array `nums`.
2. Sort the array `nums` in ascending order.
3. Initialize a result array `res` of the same length as `nums` with all elements set to 0.
4. Iterate through the sorted array `nums`. For each number, if it is different from the previous number, it means that all numbers less than it have been counted. So, we set the count of smaller numbers for each of these numbers to the current index `i`.
5. Remove the indices of the current number from the hash table `h1` to avoid counting it again.
6. Return the result array `res`.

**Time Complexity**
O(n log n) due to the sorting step, where n is the length of the input array. The subsequent steps have a linear time complexity.

**Space Complexity**
O(n) for the hash table and the result array, where n is the length of the input array.

**Key Insight**
The key insight is to take advantage of the fact that the array is sorted, which allows us to count the smaller numbers for each number in a single pass through the array. This approach avoids the need to compare each number with every other number, resulting in a more efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 2 ms (Beats 81.43%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-11-14 |
| 💻 Language | Python |