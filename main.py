
def num_words(file_text: str) -> int:
    return len(file_text.split())

def char_count(file_text: str) -> dict:
    return_dict = {}

    for char in file_text:
        char = char.lower()
        count = return_dict.get(char, 0)
        return_dict[char] = count + 1

    return return_dict

def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

        word_count = num_words(file_contents)
        char_dict = char_count(file_contents)

        print(f"--- Begin report of {path_to_file} ---")
        print(f"{word_count} words found in the document")
        print()
        print()

        for char in char_dict:
            if char not in "abcdefghijklmnopqrstuvwxyz":
                continue
            print(f"The '{char}' character was found {char_dict[char]} times")

        print("--- End report ---")


main()
