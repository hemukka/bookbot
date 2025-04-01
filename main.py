from stats import get_word_count, get_char_count, get_sorted_char_count
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def print_report(file_path, num_words, num_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for c in num_chars:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["count"]}")
    
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    num_chars_dict = get_char_count(book_text)
    sorted_num_chars = get_sorted_char_count(num_chars_dict)

    print_report(book_path, num_words, sorted_num_chars)

main()