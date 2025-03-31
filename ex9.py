N, K, R = map(int, input().split())
day = 1

while N < R:
    N += N * K / 100
    day += 1

print(day)
