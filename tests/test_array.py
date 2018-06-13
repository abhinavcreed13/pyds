#Test Array Implementation

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pyds import array

#test array
print("01 : ======= Creating Array of size 5 =======")
arr = array(5)

print("02: ======= Traversing Array =======")
arr.print()

print("03: ======= Insert 5 Items =======")
arr.insert(0,1)
arr.insert(1,2)
arr.insert(2,3)
arr.insert(3,4)
arr.insert(4,5)

print("======= Traversing Array =======")
arr.print()

print("04: ======= Exceeding Items =======")
try:
    arr.insert(5,6)
except Exception as err:
    print(err)

print("05: ======= Delete Item at index 0 =======")
print(arr.delete(0))

print("06: ======= Re-Traversing Array =======")
arr.print()


