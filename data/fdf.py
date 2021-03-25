import random

n = int(input())
types = input().split()
min_d = int(input())
dist = list(map(float, input().split()))
diameters = [i for i in range(min_d, 301, 10)]
random.shuffle(diameters)

for i in range(n):
    a = round(random.uniform(dist[0], dist[1]), 1)
    print(f'{random.choice(types)} plate size {diameters[i]}, '
          f'through {a} sm fork, fits the {round(diameters[i] / a * 10, 2)} of food.')
