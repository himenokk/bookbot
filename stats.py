def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_number(text):
    words = text.split()
    return len(words)

def count_letter(text):
    char_count = {}
    for letter in text.lower():
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
    return char_count

def sort_char(char_count):
    sorted_chars = []

    for char in char_count:
        sorted_chars.append({"char": char, "count": char_count[char]})

    sorted_chars.sort(key=lambda x: x["count"], reverse = True)

    return sorted_chars
        
