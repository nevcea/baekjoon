n = int(input())
x = list(map(int, input().split()))
m, s = max(x), sum(x)
print(s * 100 / m / int(n))