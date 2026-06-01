class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        h1 = Counter(digits)
        res = []
        for i in range(1, 10):
            check = h1.copy()
            if check[i] > 0:
                check[i] -= 1
                for j in range(10):
                    if check[j] > 0:
                        check[j] -= 1
                        for k in range(0, 10, 2):
                            if check[k] > 0:
                                res.append(i * 100 + j * 10 + k)
                        check[j]+=1
        return res
