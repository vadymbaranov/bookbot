def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_of_book_words(book_text)
    chars_dict = count_characters(book_text)
    create_book_report(num_words, chars_dict, book_path)
 
def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()
        return file_contents

def get_num_of_book_words(book_text):
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    char_dict = {}
    for char in book_text:
        lower_char = char.lower()
        if lower_char in char_dict:
            char_dict[lower_char] += 1
        else:
            char_dict[lower_char] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def create_book_report(book_words, book_chars, book_path):
    list_of_chars = create_list_of_char_dicts(book_chars)
    list_of_chars.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{book_words} words found in the document")
    for char in list_of_chars:
        char_name = char["name"]
        char_count = char["count"]
        print(f"The '{char_name}' character was found {char_count} times")
    print("--- End report ---")
    
def create_list_of_char_dicts(book_chars):
    list_of_chars = []
    for char in book_chars:
        if char.isalpha():
            list_of_chars.append({ "name": char, "count": book_chars[char] })
    return list_of_chars



main()
