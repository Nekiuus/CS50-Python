import sys

if len(sys.argv) < 2:
    sys.exit("too few arguments")
for arg in sys.argv[1:]:
    print("hello, my name is", arg)


'''
if len(sys.argv) > 2:
    sys.exit("too many arguments")
elif len(sys.argv) < 2:
    sys.exit("too few arguments")

print("hello, my name is", sys.argv[1])
'''

'''
try:
    print("hello, my name is", sys.argv[1])

except IndexError:
    print("too few arguments")
'''