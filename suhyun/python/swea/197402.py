def pro(arr):
    for i in range(9):
        ga = [0] * 10
        se = [0] * 10
        for j in range(9):
            ga[arr[i][j]] += 1
            if ga[arr[i][j]] == 2:
                return 0

            se[arr[j][i]] += 1
            if se[arr[j][i]] == 2:
                return 0
    
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            list33 = [0] * 10
            for row in range(3):
                for col in range(3):
                    list33[arr[x + row][y + col]] += 1
                    if list33[arr[x + row][y + col]] == 2:
                        return 0
    
    return 1
    
t = int(input())
for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = pro(arr)
    print(f'#{tc} {result}')
