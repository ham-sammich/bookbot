def get_word_count(content):
    word_count = len(content.split())
    print(f"{word_count} words found in the document")

def sort_on(dict):
    return dict["count"]

def get_character_count(content):
    char_dict = {}
    char_list = []
    for c in content:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c]  = 1
    for character in char_dict:
        char_list.append({"character": character, "count": char_dict[character]})
    char_list.sort(reverse=True,key=sort_on)
    for char in char_list:
        print(f"The '{char["character"]} character was found {char["count"]} times")

def main():
    file = "books/frankenstein.txt"
    with open(f"./{file}") as f:
        file_contents = f.read()
        print(f"--- Begin report of {file} ---")
        get_word_count(file_contents)
        get_character_count(file_contents.lower())
        print("--- End report ---")
main()