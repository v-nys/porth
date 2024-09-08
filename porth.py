#!/usr/bin/env/python3

counter = 0

def iota():
    global counter
    current_value = counter
    counter += 1
    return current_value

OP_PUSH = iota()
OP_PLUS = iota()
OP_DUMP = iota()
COUNT_OPS = iota()

print(f"OP_PUSH: {OP_PUSH}")
print(f"OP_PLUS: {OP_PLUS}")
print(f"OP_DUMP: {OP_DUMP}")
print(f"COUNT_OPS: {COUNT_OPS}")
