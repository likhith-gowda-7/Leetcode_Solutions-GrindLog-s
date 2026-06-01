class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for curr_ast in asteroids:
            if(mass<curr_ast):
                return False
            mass+=curr_ast
        return True