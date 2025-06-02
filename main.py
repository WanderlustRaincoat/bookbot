def main():
    book_path ="books/frankenstein.txt"
    contents = get_book_text(book_path)
    num_words = word_count(contents)
    print(f"{num_words} words found in the document")

def get_book_text(book_path):
    with open(book_path) as f:
        book_contents = f.read()
    return book_contents

def word_count(contents):
    num_words = len(contents.split())
    return num_words

main()
