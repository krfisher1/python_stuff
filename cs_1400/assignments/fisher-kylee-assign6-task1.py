import time
import random
count = 1
ranget = 0
i = 1
fluky_nums = 0
total_loops = 0 


start = time.time()
for i in range(1,10000):
    added = 0
    total_loops += 1
    for factor in range(1, i):
        if i % factor == 0:
            random.seed(factor)
            added += random.randint(1, i)
            total_loops += 1
    if added == i:
        print("Fluky Number: " + str(i))
        fluky_nums += 1
        total_loops += 1
    if fluky_nums == 7:
        break
    

end = time.time()

total_time = round((end - start), 2)
print("Number of loops " + str(total_loops))
print("Total time: " + str(total_time))


