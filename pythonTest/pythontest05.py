#!/user/bin/python3
import sys
list = [1,2,3,4]
it = iter(list)
print(next(it))
for x in it:
    print(x,end="")
print("")
list = [1,2,3,4]
it = iter(list)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()






