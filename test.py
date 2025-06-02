def get_book_text(t):
    with open(t) as f:
        file_contents = f.read()
    return file_contents
def words(file_contents):
    
    num_words = len(file_contents.split())
    
    return num_words
    
def main():
    
    book = get_book_text("books/frankenstein.txt")
    
    count = words(book)
    
    print(f"{count} words found in the document")
main()
