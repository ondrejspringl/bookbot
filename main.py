def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    list_characters = dict_to_list(num_characters)
    list_characters.sort(key=sort_on, reverse=True)
    print_report(num_words, list_characters)

def get_book_text(path):
    with open (path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    characters = {}
    lowered_text = text.lower()
    for lt in lowered_text:
        if lt in characters:
            characters[lt] += 1
        else:
            characters[lt] = 1
    return characters

def dict_to_list(num_characters):
    character_list = []
    for character, count in num_characters.items():
        character_list.append({"character": character, "num": count})
    return character_list

def sort_on(item):
    return item["num"]

def print_report(num_words, list_characters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for nc in list_characters:
        character = nc["character"]
        if character.isalpha():
            count = nc["num"]
            print(f"The '{character}' character was found {count} times")
    print("--- End report ---")


main()