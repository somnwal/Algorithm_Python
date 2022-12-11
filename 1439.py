import sys

text = sys.stdin.readline().rstrip()

count = 0

zc = sum(len(i) != 0 for i in text.split("1"))
oc = sum(len(i) != 0 for i in text.split("0"))

if zc >= oc:
    count = oc
else:
    count = zc

print(count)