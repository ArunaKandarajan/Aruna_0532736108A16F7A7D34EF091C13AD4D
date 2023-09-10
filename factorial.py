def recurfact(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * (recurfact(n - 1))


number = int(input("ENTER A NUMBER:"))
res = recurfact(number)
print(
  "THE FACTORIAL OF",
  number,
  "IS",
  res,
)
