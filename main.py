import sys

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print(f"This file contains {len(words)} words!")
    
    count_dictionary = count_characters(file_contents)
    converted_count_dictionary = convert_dictionary(count_dictionary)
    print_report(words, converted_count_dictionary)

def count_characters(my_string):
    lowered_string = my_string.lower()
    character_count = {}
    for character in lowered_string:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def convert_dictionary(my_dictionary):
    converted_list = []
    for key in my_dictionary:
        if key.isalpha():
            converted_list.append({"letter":key, "num":my_dictionary[key]})
    return converted_list        

def print_report(words, count_list):
    print ("--- Begin report of books/frankenstein.txt ---")
    #print word count
    print(f"This file contains {len(words)} words!")
    #print character count
    count_list.sort(reverse = True, key = sort_on)
    for d in count_list:
        print(f"The '{d["letter"]} character was found {d["num"]} times")

def sort_on(dict):
    return dict["num"]


if __name__ == '__main__':
    sys.exit(main())
