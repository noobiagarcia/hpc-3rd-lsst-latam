import random
import time

N = 100000000
inicio = time.time()

dentro = 0

for i in range(N):
    x = random.random()
    y = random.random()

    if x*x + y*y <= 1:
        dentro += 1

pi = 4 * dentro / N
fim = time.time()

print(f"PI={pi}")
print(f"Time: {fim - inicio:.2f} seconds")
