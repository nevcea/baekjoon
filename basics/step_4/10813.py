n, m = map(int, input().split())
x = [str(i + 1) for i in range(n)]

for __ in range(m):
  i, j = map(int, input().split())
  x[i - 1], x[j - 1] = x[j - 1], x[i - 1]

print(' '.join(x))