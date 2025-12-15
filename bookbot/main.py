"""
Small Python project (in progress).
"""
import sys
from stats import get_num_words, get_letter_count, sort_dict

def get_book_text(filepath):
    """
    Read and return the full contents of a text file.

    :param filepath: str - path to the text file
    :return: str - file contents
    """
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def main():
    print("============ BOOKBOT ============")
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print(f"Analyzing book found at {filepath[1:]}")
   
    text = get_book_text(filepath)
    print("----------- Word Count ----------")
    
    word_count = get_num_words(text)
    print(f"Found {word_count} total words")
    
    print("--------- Character Count -------")
    sorted_list = sort_dict(get_letter_count(text))
    for entry in sorted_list:
            if entry["char"].isalpha():
                print(f"{entry["char"]}: {entry["num"]}")

    print("============= END ===============")


if __name__ == "__main__":
    main()

