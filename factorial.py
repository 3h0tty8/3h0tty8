#method 1
n = 8
x = 1
for i in range(1, n+1):
  x *= i
print (x)

#method 2
def factorial(n):
  if n = 1 or n = 0:
    return 1
  else:
    return n  * factorial(n-1)
print(factorial(n))
