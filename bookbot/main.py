"""
Small Python project (in progress).
"""

def get_book_text(filepath):
    """
    Read and return the full contents of a text file.

    :param filepath: str - path to the text file
    :return: str - file contents
    """
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def count_words(text):
    """
    Count the number of words in a given text.

    Words are defined as whitespace-separated tokens.

    :param text: str - input text
    :return: int - number of words
    """
    return len(text.split())


def main():
    filepath = "./books/frankenstein.txt"
    text = get_book_text(filepath)
    word_count = count_words(text)
    print(f"Found {word_count} total words")


if __name__ == "__main__":
    main()

