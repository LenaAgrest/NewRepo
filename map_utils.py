from collections import deque

class Map:
    def __init__(self, filename):
        self.map = []
        with open(filename, encoding='utf-8') as file:
            for line in file:
                row = list(map(int, line.strip().split()))
                self.map.append(row)
        self.rows = len(self.map)
        self.cols = len(self.map[0]) if self.rows > 0 else 0

    def is_valid(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols

    def is_sea(self, r, c):
        return self.is_valid(r, c) and self.map[r][c] == 0

    def is_land(self, r, c):
        return self.is_valid(r, c) and self.map[r][c] == 1

    def find_path(self, start, goal):
        if not self.is_land(*start) or not self.is_land(*goal):
            raise ValueError("Обе точки должны быть на суше (1)")

        visited = [[False] * self.cols for _ in range(self.rows)]
        prev = [[None] * self.cols for _ in range(self.rows)]

        queue = deque()

        # Добавляем соседей начальной суши, только по морю
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = start[0] + dr, start[1] + dc
            if self.is_sea(nr, nc):
                queue.append((nr, nc))
                visited[nr][nc] = True
                prev[nr][nc] = start

        while queue:
            r, c = queue.popleft()

            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc

                if not self.is_valid(nr, nc) or visited[nr][nc]:
                    continue

                # Если достигли целевой суши
                if (nr, nc) == goal:
                    prev[nr][nc] = (r, c)
                    return self._reconstruct_path(prev, start, (nr, nc))

                if self.is_sea(nr, nc):
                    queue.append((nr, nc))
                    visited[nr][nc] = True
                    prev[nr][nc] = (r, c)

        return None  # Путь не найден

    def _reconstruct_path(self, prev, start, end):
        path = []
        cur = end
        while cur != start:
            path.append(cur)
            cur = prev[cur[0]][cur[1]]
        path.append(start)
        return path[::-1]
