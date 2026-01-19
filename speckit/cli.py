import sys

def main():
    args = sys.argv[1:]
    if not args:
        print("specify: no command provided")
        return
    cmd = args[0]
    if cmd == "init":
        print("specify: initialized")
        return
    print(f"specify: unknown command '{cmd}'")
