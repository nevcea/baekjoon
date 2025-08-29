n, m = map(int, input().split())
x = [i for i in range(1, n + 1)]

tmp = 0

for _ in range(m):
  i, j = map(int, input().split())
  tmp = x[i - 1:j]
  tmp.reverse()
  x[i - 1:j] = tmp

for i in range(n):
  print(x[i], end=" ")