import argparse

def number_lines_from_file(input_file):   
    try:
        with open(input_file, 'r') as input:
            lines = input.readlines()
        i = 1
        numbered_lines = []
        for line in lines:
            numbered_lines.append(f"{i}\t{line}")
            i += 1
        for line in numbered_lines:
            print(line, end='')

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")


def number_lines_from_input():
    i = 1
    while True:
        try:
            line = input()
            print(f"{i}\t{line}")
            i += 1
        except EOFError:
            break


def main(): 
    parser = argparse.ArgumentParser(description="Simplified nl command")
    parser.add_argument('--input_file', help="Input file")
    args = parser.parse_args()
    if args.input_file is not None: 
        number_lines_from_file(args.input_file)
    else:
        number_lines_from_input()

if __name__ == "__main__":
    main()