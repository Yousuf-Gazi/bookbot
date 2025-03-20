import sys
from stats import (
    get_number_of_words,
    count_char,
    sort_counted_char
)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    contents = get_book_text(book_path)
    total_words = get_number_of_words(contents)
    char_dict = count_char(contents)
    sorted_labeled_dicts = sort_counted_char(char_dict)
    report(book_path, total_words, sorted_labeled_dicts)


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def report(book_path, total_words, sorted_labeled_dicts,):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_labeled_dicts:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['count']}")
    print("============= END ===============")


main()