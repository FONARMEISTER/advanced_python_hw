import argparse
import sys

def wc_content(content):
    lines_count = len(content.splitlines())
    words_count = len(content.split())
    bytes_count = len(content.encode('utf-8'))
    return lines_count, words_count, bytes_count


def wc_files(input_files):   
    total_lines_count = 0
    total_words_count = 0
    total_bytes_count = 0
    for input_file in input_files:
        lines_count, words_count, bytes_count = wc_file(input_file)
        total_lines_count += lines_count
        total_words_count += words_count
        total_bytes_count += bytes_count
    print(f"{total_lines_count:8}{total_words_count:8}{total_bytes_count:8} total")


def wc_file(input_file):
    try:
        with open(input_file, 'r') as input:
            content = input.read()
        lines_count, words_count, bytes_count = wc_content(content)
        print(f"{lines_count:8}{words_count:8}{bytes_count:8} {input_file}")
        return lines_count, words_count, bytes_count

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return 0,0,0


def wc_stdin():
    content = sys.stdin.read()
    lines_count, words_count, bytes_count = wc_content(content)
    print(f"{lines_count:8}{words_count:8}{bytes_count:8}")


def main(): 
    parser = argparse.ArgumentParser(description="Simplified wc command")
    parser.add_argument('--input_files', nargs='+', help="List of input file", default=[])
    args = parser.parse_args()
    input_files = args.input_files
    if len(input_files) == 0:
        wc_stdin() 
    elif len(input_files) == 1:
        wc_file(input_files[0])
    elif len(input_files) > 1:
        wc_files(input_files)
    else:
        print("Error: incorrect input format")

if __name__ == "__main__":
    main()