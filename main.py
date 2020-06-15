import sys
from source.machine import Machine

if __name__ == "__main__":
    with open('test1.cor', 'rb') as stream:
        contents = stream.read()
    if len(contents) % 4 != 0:
        raise ValueError
    contents = [
        int.from_bytes(contents[i:i + 4], 'little')
        for i in range(0, len(contents), 4)
    ]

    with open('test2.cor', 'rb') as stream:
        contents2 = stream.read()
    if len(contents2) % 4 != 0:
        raise ValueError
    contents2 = [
        int.from_bytes(contents2[i:i + 4], 'little')
        for i in range(0, len(contents2), 4)
    ]

    machine = Machine(contents, contents2)
    machine.run()
    print(machine.status(), " won")