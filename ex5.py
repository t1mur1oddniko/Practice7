N = int(input())
side = 1
while (volume := side**3) <= N:
    print(volume, end=' ')
    side += 1
