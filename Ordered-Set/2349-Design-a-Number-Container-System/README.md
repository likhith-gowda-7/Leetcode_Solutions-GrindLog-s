> 📌 **Cross-listed:** Primary location is [Hash Table/2349-Design-a-Number-Container-System](../../Hash-Table/2349-Design-a-Number-Container-System). This problem also appears under: **Hash Table**, **Design**, **Heap (Priority Queue)**, **Ordered Set**

# 2349. Design a Number Container System


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Design](https://img.shields.io/badge/Design-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple) ![Ordered Set](https://img.shields.io/badge/Ordered%20Set-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/design-a-number-container-system/)


## 📝 Problem Description

Design a number container system that can do the following:

	- **Insert **or **Replace** a number at the given index in the system.

	- **Return **the smallest index for the given number in the system.

Implement the `NumberContainers` class:

	- `NumberContainers()` Initializes the number container system.

	- `void change(int index, int number)` Fills the container at `index` with the `number`. If there is already a number at that `index`, replace it.

	- `int find(int number)` Returns the smallest index for the given `number`, or `-1` if there is no index that is filled by `number` in the system.

 

Example 1:**

```

**Input**
["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
**Output**
[null, -1, null, null, null, null, 1, null, 2]

**Explanation**
NumberContainers nc = new NumberContainers();
nc.find(10); // There is no index that is filled with number 10. Therefore, we return -1.
nc.change(2, 10); // Your container at index 2 will be filled with number 10.
nc.change(1, 10); // Your container at index 1 will be filled with number 10.
nc.change(3, 10); // Your container at index 3 will be filled with number 10.
nc.change(5, 10); // Your container at index 5 will be filled with number 10.
nc.find(10); // Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index that is filled with 10 is 1, we return 1.
nc.change(1, 20); // Your container at index 1 will be filled with number 20. Note that index 1 was filled with 10 and then replaced with 20. 
nc.find(10); // Number 10 is at the indices 2, 3, and 5. The smallest index that is filled with 10 is 2. Therefore, we return 2.

```

 

**Constraints:**

	- `1 <= index, number <= 10^9`

	- At most `10^5` calls will be made **in total** to `change` and `find`.

## 🧠 Solution Explanation

**Intuition**
The solution utilizes two hash tables to efficiently manage the number container system. The first hash table (`h1`) stores numbers as keys and their corresponding indices as a sorted set, allowing for quick retrieval of the smallest index for a given number. The second hash table (`h2`) maps indices to their corresponding numbers, facilitating fast replacement of numbers at specific indices.

**Approach**
1. Initialize two hash tables (`h1` and `h2`) in the `NumberContainers` constructor.
2. In the `change` method:
   - Check if the index already exists in `h2`. If it does, remove the index from the sorted set of indices for the current number in `h1`.
   - Add the index to the sorted set of indices for the new number in `h1`.
   - Update the value in `h2` with the new number.
3. In the `find` method:
   - Check if the sorted set of indices for the given number in `h1` is not empty.
   - If it's not empty, return the smallest index from the set.
   - Otherwise, return -1.

**Time Complexity**
- `change`: O(log n) due to the insertion and removal operations in the sorted set of indices for the number in `h1`.
- `find`: O(log n) to retrieve the smallest index from the sorted set of indices for the number in `h1`.

**Space Complexity**
- O(n) to store the numbers and their corresponding indices in the two hash tables.

**Key Insight**
The key to this solution is the use of a sorted set to store the indices for each number, allowing for efficient retrieval of the smallest index for a given number. This approach enables the `NumberContainers` class to efficiently manage the number container system while maintaining a time complexity of O(log n) for both the `change` and `find` methods.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 636 ms (Beats 5.38%) |
| 💾 Memory | 151.8 MB (Beats 6.99%) |
| 📅 Solved | 2025-02-08 |
| 💻 Language | Python |