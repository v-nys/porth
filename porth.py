#!/usr/bin/env/python3
import sys

counter = 0

def iota(reset=False):
    global counter
    if reset:
        counter = 0
    current_value = counter
    counter += 1
    return current_value

OP_PUSH = iota(reset=True)
OP_PLUS = iota()
OP_MINUS = iota()
OP_DUMP = iota()
COUNT_OPS = iota()

print(f"OP_PUSH: {OP_PUSH}")
print(f"OP_PLUS: {OP_PLUS}")
print(f"OP_MINUS: {OP_MINUX}")
print(f"OP_DUMP: {OP_DUMP}")
print(f"COUNT_OPS: {COUNT_OPS}")

def push(x):
    return (OP_PUSH, x)

def plus():
    return (OP_PLUS,) # single-element tuple

def minus():
    return (OP_MINUS,) # single-element tuple

def dump():
    return (OP_DUMP,) # single-element tuple

def simulate_program(program):
    stack = []
    for op in program:
        # maybe use pattern match?
        assert COUNT_OPS == 4, "Exhaustive handling of operations in simulation"
        if op[0] == OP_PUSH:
            stack.append(op[1])
        elif op[0] == OP_PLUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif op[0] == OP_MINUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
         elif op[0] == OP_DUMP:
            a = stack.pop()
            print(a)
        else:
            assert False, "unreachable (operator should not exist)"

def compile_program(program):
    assert False, "Not implemented"


program=[
  push(34),
  push(35),
  plus(),
  dump()
]

def usage():
    print("Usage: porth <SUBCOMMAND> [ARGS]")
    print("SUBCOMMANDS")
    print("    sim    Simulate the program")
    print("    com    Compile the program")


if __name__ == '__main__':
    # Kan eventueel click of iets gelijkaardigs gebruiken...
    if len(sys.argv) < 2:
        usage()
    subcommand = sys.argv[1]
    if subcommand == "sim":
        simulate_program(program)
    elif subcommand == "com":
        compile_program(program)
    else:
        usage()
        print(f"ERROR: unknown subcommand {subcommand}")
        exit(1)
