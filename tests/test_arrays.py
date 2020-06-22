import sys
sys.path.append('src/')
sys.path.append('../src/')
from arrays import Arrays

arr = Arrays(100, 0, 100)
print(arr.giveArray())

print(arr.generateArray(arr.SIZE, arr.LEFT, arr.RIGHT))