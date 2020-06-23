import sys
sys.path.append('src/')
sys.path.append('../src/')

from arrays import Arrays

count=0
for _ in range(10000):
    arr = Arrays(100, 0, 100)
    print(arr.giveArray())
    print(arr.generateArray(arr.SIZE, arr.LEFT, arr.RIGHT))
    count=count+1

if(count==10000):
    print(f'Test finished completely')