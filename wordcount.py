import sys
import collections


def print_count(file_name):
    """ Prints one per line '<word> <count>' sorted by word for the given file """
    words = open(file_name).read().lower().split()
    words = collections.Counter(words).most_common()
    for word in words:
        print(word[0], word[1])


def print_top(file_name):
    """  Prints the top count listing for the given file """
    words = open(file_name).read().lower().split()
    top_20 = collections.Counter(words).most_common(20)
    for most_populated in top_20:
        print(most_populated[0], most_populated[1])


def main():
    if len(sys.argv) != 3:
        print('Usage: ./wordcount.py {--count | --top} <file name>')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_count(filename)
    elif option == '--top':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
