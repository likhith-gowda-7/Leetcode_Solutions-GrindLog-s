> 📌 **Cross-listed:** Primary location is [Array/1700-Number-of-Students-Unable-to-Eat-Lunch](../../Array/1700-Number-of-Students-Unable-to-Eat-Lunch). This problem also appears under: **Array**, **Stack**, **Queue**, **Simulation**

# 1700. Number of Students Unable to Eat Lunch


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Queue](https://img.shields.io/badge/Queue-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/)


## 📝 Problem Description

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers `0` and `1` respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a **stack**. At each step:

	- If the student at the front of the queue **prefers** the sandwich on the top of the stack, they will **take it** and leave the queue.

	- Otherwise, they will **leave it** and go to the queue's end.

This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays `students` and `sandwiches` where `sandwiches[i]` is the type of the `i^​​​​​​th` sandwich in the stack (`i = 0` is the top of the stack) and `students[j]` is the preference of the `j^​​​​​​th` student in the initial queue (`j = 0` is the front of the queue). Return *the number of students that are unable to eat.*

 

Example 1:**

```

**Input:** students = [1,1,0,0], sandwiches = [0,1,0,1]
**Output:** 0** 
Explanation:**
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.

```

Example 2:**

```

**Input:** students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
**Output:** 3

```

 

**Constraints:**

	- `1 <= students.length, sandwiches.length <= 100`

	- `students.length == sandwiches.length`

	- `sandwiches[i]` is `0` or `1`.

	- `students[i]` is `0` or `1`.

## 🧠 Solution Explanation

**Intuition**
The solution works by maintaining a count of the number of students who prefer square and circular sandwiches, and simulating the process of students taking sandwiches from the stack. The key insight is to realize that once a student who prefers a different type of sandwich reaches the front of the queue, the process will terminate, and the number of students unable to eat will be the size of the remaining queue.

**Approach**
1. Initialize two variables `types` to store the count of students who prefer square and circular sandwiches.
2. Count the occurrences of `0` and `1` in the `students` array and store them in `types`.
3. Create a queue `q` from the `students` array.
4. While the queue is not empty, pop the front student and check if they prefer the top sandwich in the stack.
5. If they do, decrement the count of their preferred sandwich type and remove the top sandwich from the stack.
6. If they don't, append them to the end of the queue.
7. If the count of the preferred sandwich type of the top sandwich in the stack is zero, break the loop.
8. Return the size of the remaining queue.

**Time Complexity**
O(n), where n is the number of students. This is because we iterate through the queue once, and each operation (popping, appending, decrementing count) takes constant time.

**Space Complexity**
O(n), where n is the number of students. This is because we store the entire `students` array in the queue.

**Key Insight**
The key insight is to realize that once a student who prefers a different type of sandwich reaches the front of the queue, the process will terminate, and the number of students unable to eat will be the size of the remaining queue. This is because the students who prefer the same type of sandwich as the top sandwich in the stack will continue to take sandwiches until they are all gone.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-11-21 |
| 💻 Language | Python |