def main():
    book_path = "books/frankenstein.txt" # Gets book path
    text = get_book_text(book_path) # Gets text from book path
    num_words = get_num_words(text) # Gets number of words from text
    char_dict = get_char_dict(text) # Gets number of characters from text save into dictionary with keys
    char_sorted = char_dict_to_sorted(char_dict) # Gets report from book_path, num_words, and char_dict
    
    # Print Report
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in char_sorted: # For each char in the sorted list
        if not item["char"].isalpha(): # If the character is not a character in the alphabet
            continue
        print(f"The '{item['char']} character was found {item['num']} times")

    print(f"--- End report ---")

def get_num_words(text): # Gets number of words from the text
    words = text.split() # Splits text by whitespace, making a list of words
    return len(words) # Returns the length of the words lsit

def get_book_text(path): # Gets text from the book file
    with open(path) as f: # Opens file as f
        return f.read() # Reads the text file and returns string
    
def get_char_dict(text): # Gets number of characters from the text and saved into dictionary of each letter
    lowercase_text = text.lower() # Uses lower function tto make the string all lowercase
    char_counts = {} # Makes an empty dictionary for character counts

    for char in lowercase_text: # For every character in the text
        if char in char_counts: # If character already in dictionary
            char_counts[char] += 1 # add 1 to the value
        else:
            char_counts[char] = 1 # Set value to one with char key
        
    return char_counts # Returns character count

def sort_on(dict):
    return dict["num"] # Tells sort which metric to sort by

def char_dict_to_sorted(num_chars_dict):
    sorted = [] # Creates new list for sorted chars
    for ch in num_chars_dict: # For character in the dictionary
        sorted.append({"char": ch, "num": num_chars_dict[ch]}) # For every character in num_chars_dict, append sorted with char and then the character and the value(total) as num
    sorted.sort(reverse=True, key=sort_on) # Uses python sort and reverses it using the key sort_on. Goes by num in descending order now
    return sorted


main()