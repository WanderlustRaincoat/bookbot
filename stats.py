def word_count(contents):
    num_words = len(contents.split())
    return num_words

def char_count(contents):
    lower_char = contents.lower()
    values = {}
    for char in lower_char:
        if char not in values:
            values[char] = 1
        else:
            values[char] += 1
    return values
def sort_on(dict):
    return dict["num"]

def list_sort(chars):
    list = []
    for char, value in chars.items():
        entry = {"char": char, "num": value}
        list.append(entry)
    list.sort(reverse=True, key=sort_on)
    return list
