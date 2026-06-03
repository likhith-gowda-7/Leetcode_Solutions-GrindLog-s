# 2126. Destroying Asteroids


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/destroying-asteroids/)


## 📝 Problem Description

You are given an integer `mass`, which represents the original mass of a planet. You are further given an integer array `asteroids`, where `asteroids[i]` is the mass of the `i^th` asteroid.

You can arrange for the planet to collide with the asteroids in **any arbitrary order**. If the mass of the planet is **greater than or equal to** the mass of the asteroid, the asteroid is **destroyed** and the planet **gains** the mass of the asteroid. Otherwise, the planet is destroyed.

Return `true`* if **all** asteroids can be destroyed. Otherwise, return *`false`*.*

 

Example 1:**

```

**Input:** mass = 10, asteroids = [3,9,19,5,21]
**Output:** true
**Explanation:** One way to order the asteroids is [9,19,5,3,21]:
- The planet collides with the asteroid with a mass of 9. New planet mass: 10 + 9 = 19
- The planet collides with the asteroid with a mass of 19. New planet mass: 19 + 19 = 38
- The planet collides with the asteroid with a mass of 5. New planet mass: 38 + 5 = 43
- The planet collides with the asteroid with a mass of 3. New planet mass: 43 + 3 = 46
- The planet collides with the asteroid with a mass of 21. New planet mass: 46 + 21 = 67
All asteroids are destroyed.

```

Example 2:**

```

**Input:** mass = 5, asteroids = [4,9,23,4]
**Output:** false
**Explanation:** 
The planet cannot ever gain enough mass to destroy the asteroid with a mass of 23.
After the planet destroys the other asteroids, it will have a mass of 5 + 4 + 9 + 4 = 22.
This is less than 23, so a collision would not destroy the last asteroid.
```

 

**Constraints:**

	- `1 <= mass <= 10^5`

	- `1 <= asteroids.length <= 10^5`

	- `1 <= asteroids[i] <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution works by sorting the asteroids in ascending order and then iterating through them. If the current asteroid's mass is greater than the planet's mass, the function immediately returns `False` because the planet cannot destroy the asteroid. If the planet's mass is sufficient to destroy the asteroid, the function updates the planet's mass and continues to the next asteroid.

**Approach**
1. Sort the asteroids array in ascending order.
2. Iterate through the sorted asteroids array.
3. For each asteroid, check if the planet's mass is less than the asteroid's mass.
4. If the planet's mass is less than the asteroid's mass, return `False`.
5. If the planet's mass is greater than or equal to the asteroid's mass, add the asteroid's mass to the planet's mass.
6. After iterating through all asteroids, return `True`.

**Time Complexity**
O(n log n) due to the sorting operation, where n is the number of asteroids.

**Space Complexity**
O(1) because the sorting operation is done in-place, and the iteration through the asteroids array only requires a constant amount of extra space.

**Key Insight**
The key insight is that if the planet's mass is sufficient to destroy an asteroid, it will also be sufficient to destroy all smaller asteroids. Therefore, we can sort the asteroids in ascending order and iterate through them, checking if the planet's mass is sufficient to destroy each one. This greedy approach allows us to efficiently determine if all asteroids can be destroyed.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 71 ms (Beats 73.97%) |
| 💾 Memory | 34.1 MB (Beats 30.33%) |
| 📅 Solved | 2026-05-31 |
| 💻 Language | Python |