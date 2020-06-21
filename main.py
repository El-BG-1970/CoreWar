import sys, os
from source.machine import Machine

if __name__ == "__main__":
    args = [str(i) for i in sys.argv[1:]]
    if len(args) in [0,1,2]:
        print("syntax: python corewar.py <max_turns> <program1> <program2>")
        sys.exit(-1)
    elif len(args) > 3:
        print("too many arguments")
        sys.exit(-1)

    if not os.path.exists(args[1]):
        print('invalid file for program1')
        sys.exit(-1)
    if not os.path.exists(args[2]):
        print('invalid file for program2')
        sys.exit(-1)
    with open(args[1], 'rb') as stream:
        contents = stream.read()
    if len(contents) % 4 != 0:
        raise ValueError
    contents = [
        int.from_bytes(contents[i:i + 4], 'little')
        for i in range(0, len(contents), 4)
    ]

    with open(args[2], 'rb') as stream:
        contents2 = stream.read()
    if len(contents2) % 4 != 0:
        raise ValueError
    contents2 = [
        int.from_bytes(contents2[i:i + 4], 'little')
        for i in range(0, len(contents2), 4)
    ]

    machine = Machine(contents, contents2, int(args[0]))
    machine.run()
    print(machine.status(), " won")