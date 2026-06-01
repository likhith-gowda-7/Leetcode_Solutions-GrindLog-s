class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        q = deque()

        # Step 1: Collect all border "O"s
        def addBorder(r, c):
            if 0 <= r < m and 0 <= c < n and board[r][c] == "O":
                q.append((r, c))
                board[r][c] = "B"   # mark as border-connected

        for r in range(m):
            addBorder(r, 0)
            addBorder(r, n - 1)
        for c in range(n):
            addBorder(0, c)
            addBorder(m - 1, c)

        # Step 2: Multi-source BFS from all border "O"s
        while q:
            r, c = q.popleft()
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "O":
                    board[nr][nc] = "B"
                    q.append((nr, nc))

        # Step 3: Flip regions
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":  # not connected to border → capture
                    board[r][c] = "X"
                elif board[r][c] == "B":  # restore border-connected "O"
                    board[r][c] = "O"
