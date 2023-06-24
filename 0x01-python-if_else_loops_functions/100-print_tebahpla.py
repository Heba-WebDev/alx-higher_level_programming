#!/usr/bin/python3

x = 122
output = ""
while (x >= 97):
    if (x % 2 == 0):
        output += "{}".format(chr(x))
        x = x - 1
    else:
        output += "{}".format(chr(x-32))
        x = x - 1
print(output)
