import sys
n = int(sys.stdin.readline())
col = [0 for _ in range(n)]
ans = 0

def attackable(r1, c1, r2, c2):
    if c1 == c2:
        return True
    if r1 - c1 == r2 - c2:
        return True
    if r1 + c1 == r2 + c2:
        return True
    return False

def pro(row):
    for cand in range(n):
        possible = True
        for i in range(row):
            if attackable(row, cand, i, col[i]):
                possible = False
                break
        
        if possible:
            col[row] = cand
            pro(row + 1)
            col[row] = 0

pro(0)
print(ans)

