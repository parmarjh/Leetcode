"""

    this testing program is for see is there any improvement on search function or not !!
    alias_name of function will decrease time 20-30% (depends on operation)
    reason is python is searching function name "len" in every iteration.
    so better to give alias of searching function and will know exact there where it needs to point.

"""
import time
arr = [1,2,3,4,5]
init_time = time.time()
print("before loop 1", time.time()-init_time)
for i in range(10000000):
    temp = len(arr)
print("after loop 1", time.time()-init_time)

len_alias = len
init_time = time.time()
print("before loop 2", time.time()-init_time)
for i in range(10000000):
    temp = len_alias(arr)
print("after loop 2", time.time()-init_time)