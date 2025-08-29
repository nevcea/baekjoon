n, m = map(int, input().split())
x = [0] * n

for _ in range(m):
  i, j, k = map(int, input().split())
  for y in range(i, j + 1): 
    x[y - 1] = k

for z in range(n):
  print(x[z], end=" ")