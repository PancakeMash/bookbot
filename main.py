def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        return file_contents

def count_words():
    new_array = main().split()

    return print(len(new_array))

def count_characters():
    letter_dict = {}
    array_lower = main().lower().split()

    for word in array_lower:
        for i in range(0,len(word)):
            if word[i] in letter_dict:
                letter_dict[word[i]] = letter_dict[word[i]] + 1
            else:
                letter_dict[word[i]] = 1

    return letter_dict

def print_count_chara():
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words} words found in the document.")
    for key, in count_characters():
        print(f"key: {key}, value: {count_characters()[key]}")
    print("--- End report ---")


main()
print_count_chara()
