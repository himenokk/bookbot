from stats import get_book_text, count_number, count_letter, sort_char
import sys

def main():

    if len(sys.argv) != 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)

    book_path = sys.argv[1]


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)
    num_of_words = count_number(text)
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")

    char_counts = count_letter(text)
    sorted_characters = sort_char(char_counts)

    print("--------- Character Count -------")
    for entry in sorted_characters:
        print(f"{entry['char']}: {entry['count']}")

    print("============= END ===============")



main()
