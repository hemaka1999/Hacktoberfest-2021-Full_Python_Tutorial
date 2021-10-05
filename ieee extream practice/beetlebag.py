t = int(input())
while t:
    C, N = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(N)]
    f = [[0] * (C + 1) for _ in range(N + 1)]
    i = 1
    while i < N + 1:
        j = 1
        while j < C + 1:
            new_j = j - g[i - 1][0]
            if new_j < 0:
                f[i][j] = f[i - 1][j]
                j += 1
                continue
            f[i][j] = max(f[i - 1][j], g[i - 1][1] + f[i - 1][new_j])
            j += 1
        i += 1
    print(f[-1][-1])
    t -= 1
