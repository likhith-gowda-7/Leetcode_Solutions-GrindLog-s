class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_order=list(zip(position,speed))
        #sort cars descending order(car that is nearest to target comes first)
        car_order.sort(reverse=True)
        stack=[]
        for car_pos,sp in car_order:
            time_taken=(target-car_pos)/sp
            stack.append(time_taken)
            if(len(stack)>1 and stack[-1]<=stack[-2]):
                stack.pop()
        return len(stack)