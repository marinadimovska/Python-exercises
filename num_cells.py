def numCells(grid):
    n = len(grid)
    m = len(grid[0])

    def is_dominant(i, j):
        current_value = grid[i][j]
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m and (ni != i or nj != j):
                    if grid[ni][nj] >= current_value:
                        return False
        return True

    count = 0
    for i in range(n):
        for j in range(m):
            if is_dominant(i, j):
                count += 1

    return count


def main():
    n = int(input())
    m = int(input())

    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    print(numCells(grid))


if __name__ == "__main__":
    main()
