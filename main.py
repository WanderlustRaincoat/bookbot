from stats import word_count
from stats import char_count
from stats import list_sort
import sys

def main():
    if len(sys.argv) < 2:
       sys.exit('Usage: python3 main.py <path_to_book>')
    book_path = sys.argv[1]
    contents = get_book_text(book_path)
    num_words = word_count(contents)
    chars = char_count(contents)
    final = list_sort(chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in final:
        char = entry.get('char', '')
        if char.isalpha():
            count = entry.get('num', 'Unknown')
            print(f"{char}: {count}")
    print("============= END ===============")

def get_book_text(book_path):
    with open(book_path) as f:
        book_contents = f.read()
    return book_contents

main()
