import sys
sys.path.append('../src/')
from arrays import Arrays

arr = Arrays(100, 0, 100)
arr.giveList()

arr.generateArray(arr.SIZE, arr.LEFT, arr.RIGHT)