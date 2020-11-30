arr = []
n = int(input())
if n <= 20:
  for i in range(n):
    x = int(input())
    arr.append(x)

arr.append(1)


def dnc(arr, l, r):
  if l > r:
    return 0
  if l == r:
    return arr[l] * arr[l - 1] * arr[l + 1]
  m = float('-inf')
  for i in range(l, r + 1):
    m = max(m, dnc(arr, l, i - 1) + dnc(arr, i + 1, r) +
            (arr[i] * arr[l - 1] * arr[r + 1]))
  return m

print(dnc(arr, 0, n-1))