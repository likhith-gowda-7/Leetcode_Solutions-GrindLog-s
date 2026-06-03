# 2210. Count Hills and Valleys in an Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-hills-and-valleys-in-an-array/)


## 📝 Problem Description

You are given a **0-indexed** integer array `nums`. An index `i` is part of a **hill** in `nums` if the closest non-equal neighbors of `i` are smaller than `nums[i]`. Similarly, an index `i` is part of a **valley** in `nums` if the closest non-equal neighbors of `i` are larger than `nums[i]`. Adjacent indices `i` and `j` are part of the **same** hill or valley if `nums[i] == nums[j]`.

Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on **both** the left and right of the index.

Return *the number of hills and valleys in *`nums`.

 

Example 1:**

```

**Input:** nums = [2,4,1,1,6,5]
**Output:** 3
**Explanation:**
At index 0: There is no non-equal neighbor of 2 on the left, so index 0 is neither a hill nor a valley.
At index 1: The closest non-equal neighbors of 4 are 2 and 1. Since 4 > 2 and 4 > 1, index 1 is a hill. 
At index 2: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 2 is a valley.
At index 3: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 3 is a valley, but note that it is part of the same valley as index 2.
At index 4: The closest non-equal neighbors of 6 are 1 and 5. Since 6 > 1 and 6 > 5, index 4 is a hill.
At index 5: There is no non-equal neighbor of 5 on the right, so index 5 is neither a hill nor a valley. 
There are 3 hills and valleys so we return 3.

```

Example 2:**

```

**Input:** nums = [6,6,5,5,4,1]
**Output:** 0
**Explanation:**
At index 0: There is no non-equal neighbor of 6 on the left, so index 0 is neither a hill nor a valley.
At index 1: There is no non-equal neighbor of 6 on the left, so index 1 is neither a hill nor a valley.
At index 2: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 2 is neither a hill nor a valley.
At index 3: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 3 is neither a hill nor a valley.
At index 4: The closest non-equal neighbors of 4 are 5 and 1. Since 4 < 5 and 4 > 1, index 4 is neither a hill nor a valley.
At index 5: There is no non-equal neighbor of 1 on the right, so index 5 is neither a hill nor a valley.
There are 0 hills and valleys so we return 0.

```

 

**Constraints:**

	- `3 <= nums.length <= 100`

	- `1 <= nums[i] <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through the array and checking each element to see if it's a hill or valley. A hill is defined as an element that is greater than its neighbors, and a valley is defined as an element that is less than its neighbors. The solution uses a while loop to skip over duplicate elements and ensure that it's checking the correct neighbors.

**Approach**
1. Initialize a counter to keep track of the number of hills and valleys.
2. Iterate through the array, starting from the second element and ending at the second last element.
3. For each element, check if it's the same as the previous element. If it is, skip to the next element.
4. If the current element is not the same as the previous element, set the left neighbor to the previous element and the right neighbor to the element after the current element.
5. Use a while loop to skip over duplicate elements on the right side of the current element.
6. Check if the current element is a hill or valley by comparing it to its neighbors. If it's a hill or valley, increment the counter.
7. Return the total count of hills and valleys.

**Time Complexity**
O(n), where n is the length of the array. This is because we're iterating through the array once, and the while loop inside the for loop has a maximum of n iterations.

**Space Complexity**
O(1), because we're using a constant amount of space to store the counter and the left and right neighbors.

**Key Insight**
The key insight here is to use a while loop to skip over duplicate elements, which allows us to efficiently check the correct neighbors for each element. This is important because we need to ensure that we're checking the correct neighbors to accurately determine whether an element is a hill or valley.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-07-27 |
| 💻 Language | Python |