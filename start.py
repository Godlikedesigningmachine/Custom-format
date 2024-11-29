import sys
import load
import convert

def main(state, custom_path, original_path=''):
    if state == "load":
        load.startup(custom_path)
    elif state == "convert":
        convert.main(original_path, custom_path)
    else:
        print("Invalid state. Use 'load' or 'convert'.")

def validate_args(args):
    if len(args) < 2:
        print("Insufficient arguments provided.")
        return False

    state = args[1]
    if state == "load":
        if len(args) != 3:
            print("Usage: script.py load <custom_path>")
            return False
    elif state == "convert":
        if len(args) != 4:
            print("Usage: script.py convert <original_path> <custom_path>")
            return False
    else:
        print(f"Unknown state: {state}")
        return False

    return True

if __name__ == "__main__":
    if not validate_args(sys.argv):
        sys.exit(1)

    state = sys.argv[1]
    if state == "load":
        custom_path = sys.argv[2]
        main(state, custom_path)
    elif state == "convert":
        original_path = sys.argv[2]
        custom_path = sys.argv[3]
        main(state, custom_path, original_path)
