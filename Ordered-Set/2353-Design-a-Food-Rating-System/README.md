> 📌 **Cross-listed:** Primary location is [Array/2353-Design-a-Food-Rating-System](../../Array/2353-Design-a-Food-Rating-System). This problem also appears under: **Array**, **Hash Table**, **String**, **Design**, **Heap (Priority Queue)**, **Ordered Set**

# 2353. Design a Food Rating System


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Design](https://img.shields.io/badge/Design-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/design-a-food-rating-system/)


## 📝 Problem Description

Design a food rating system that can do the following:

	- **Modify** the rating of a food item listed in the system.

	- Return the highest-rated food item for a type of cuisine in the system.

Implement the `FoodRatings` class:

	- `FoodRatings(String[] foods, String[] cuisines, int[] ratings)` Initializes the system. The food items are described by `foods`, `cuisines` and `ratings`, all of which have a length of `n`.

	
		- `foods[i]` is the name of the `i^th` food,

		- `cuisines[i]` is the type of cuisine of the `i^th` food, and

		- `ratings[i]` is the initial rating of the `i^th` food.

	
	

	- `void changeRating(String food, int newRating)` Changes the rating of the food item with the name `food`.

	- `String highestRated(String cuisine)` Returns the name of the food item that has the highest rating for the given type of `cuisine`. If there is a tie, return the item with the **lexicographically smaller** name.

Note that a string `x` is lexicographically smaller than string `y` if `x` comes before `y` in dictionary order, that is, either `x` is a prefix of `y`, or if `i` is the first position such that `x[i] != y[i]`, then `x[i]` comes before `y[i]` in alphabetic order.

 

Example 1:**

```

**Input**
["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
**Output**
[null, "kimchi", "ramen", null, "sushi", null, "ramen"]

**Explanation**
FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
foodRatings.highestRated("korean"); // return "kimchi"
                                    // "kimchi" is the highest rated korean food with a rating of 9.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // "ramen" is the highest rated japanese food with a rating of 14.
foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "sushi"
                                      // "sushi" is the highest rated japanese food with a rating of 16.
foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // Both "sushi" and "ramen" have a rating of 16.
                                      // However, "ramen" is lexicographically smaller than "sushi".

```

 

**Constraints:**

	- `1 <= n <= 2 * 10^4`

	- `n == foods.length == cuisines.length == ratings.length`

	- `1 <= foods[i].length, cuisines[i].length <= 10`

	- `foods[i]`, `cuisines[i]` consist of lowercase English letters.

	- `1 <= ratings[i] <= 10^8`

	- All the strings in `foods` are **distinct**.

	- `food` will be the name of a food item in the system across all calls to `changeRating`.

	- `cuisine` will be a type of cuisine of **at least one** food item in the system across all calls to `highestRated`.

	- At most `2 * 10^4` calls **in total** will be made to `changeRating` and `highestRated`.

## 🧠 Solution Explanation

**Intuition**
This solution leverages a combination of a hash map and a heap data structure to efficiently manage the food rating system. The hash map allows for fast lookups of food items and their corresponding cuisines, while the heap enables efficient retrieval of the highest-rated food item for a given cuisine.

**Approach**
1. Initialize a hash map `self.food_map` to store the cuisine of each food item, and a hash map `self.details` to store the food items for each cuisine in a min-heap.
2. Iterate through the input lists `foods`, `cuisines`, and `ratings` to populate the `self.food_map` and `self.details` hash maps.
3. For each cuisine, use the `heapify` function to transform the list of food items into a min-heap.
4. When changing the rating of a food item, update the rating in the `self.food_map` hash map and use the `heappush` function to update the heap of food items for the corresponding cuisine.
5. When retrieving the highest-rated food item for a cuisine, use the `heappop` function to remove the top-rated food item from the heap and return its name.

**Time Complexity**
- `O(n log n)` for the initial population of the hash maps and heaps, where `n` is the number of food items.
- `O(log n)` for the `changeRating` and `highestRated` operations, since they involve updating or retrieving a single food item from the heap.

**Space Complexity**
- `O(n)` for the hash maps `self.food_map` and `self.details`, which store the food items and their corresponding cuisines.

**Key Insight**
The key to this solution is the use of a min-heap to efficiently retrieve the highest-rated food item for a given cuisine. By storing the food items in a heap, we can quickly identify the top-rated item and update the heap as ratings change. This approach allows us to solve the problem in near-constant time for the `changeRating` and `highestRated` operations.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 109 ms (Beats 47.78%) |
| 💾 Memory | 52.8 MB (Beats 16.94%) |
| 📅 Solved | 2025-09-17 |
| 💻 Language | Python |