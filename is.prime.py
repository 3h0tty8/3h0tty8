a = input("")
owq = False

for i in range(2, a):
  if a % i == 0:
    owq = True
    break
if owq:
  print("prime number")
