x, n = int(input()), int(input())

r = 0
for i in range(0, n):
  a, b = map(int, input().split())
  r += (a * b)

if x == r: print("Yes")
else: print("No")