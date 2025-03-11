import argparse
import sys

def tail_file(input_file):
    try:
        with open(input_file, 'r') as input:
            lines = input.readlines()
        print(*lines[-10:], sep = '')

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")


def tail_files(input_files):   
    try:
        for input_file in input_files:
            print(f"<=={input_file}==>")
            tail_file(input_file)
            print()

    except FileNotFoundError:
        print(f"Error: File '{input_files}' not found.")


def tail_stdin():
    lines = sys.stdin.readlines()
    print(*lines[-17:], sep = '')


def main(): 
    parser = argparse.ArgumentParser(description="Simplified tail command")
    parser.add_argument('--input_files', nargs='+', help="List of input file", default=[])
    args = parser.parse_args()
    input_files = args.input_files
    if len(input_files) == 0:
        tail_stdin() 
    elif len(input_files) == 1:
        tail_file(input_files[0])
    elif len(input_files) > 1:
        tail_files(input_files)
    else:
        print("Error: incorrect input format")

if __name__ == "__main__":
    main()