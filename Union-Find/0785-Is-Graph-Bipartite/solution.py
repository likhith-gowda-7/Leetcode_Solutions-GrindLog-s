class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [None] * n

        for start in range(n):
            if color[start] is not None:
                continue

            queue = deque([start])
            color[start] = 0

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] is None:
                        color[neighbor] = color[node] ^ 1
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
        return True