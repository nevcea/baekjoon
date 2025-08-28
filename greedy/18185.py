N = int(input())
a = list(map(int, input().split()))

cost = 0

for i in range(N):
  x = 0

  if i <= N - 3 and a[i + 1] > a[i + 2]:
    x = (min(a[i], a[i + 1] - a[i + 2]))
    cost += 5 * x
    a[i] -= x
    a[i + 1] -= x

    y = min(a[i], a[i + 1], a[i + 2])
    cost += 7 * y
    a[i] -= y
    a[i + 1] -= y
    a[i + 2] -= y

  elif i <= N - 3:
    x = (min(a[i], a[i + 1], a[i + 2]))
    cost += 7 * x
    a[i] -= x
    a[i + 1] -= x
    a[i + 2] -= x
  
  elif i <= N - 2:
    x = (min(a[i], a[i + 1]))
    cost += 5 * x
    a[i] -= x
    a[i + 1] -= x

  cost += 3 * a[i]

print(cost)