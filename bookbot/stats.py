def get_help_sort(item):
    return item["num"]


def sort_dict(count_letters):
    """
    Refactor dictionary into list with etries.

    Sort by the number of occurencies 

    :param count_letters: dict passed from get_letter_count
    :return sorted_list: list with entries in the format "char" letter and "num" count_letter
    """
    sorted_list = []

    for letter in count_letters:
        entry = {"char": letter, "num": count_letters[letter]}
        sorted_list.append(entry)
    sorted_list.sort(reverse = True, key=get_help_sort)
    return sorted_list


def get_num_words(text):
    """
    Count the number of words in a given text.

    Words are defined as whitespace-separated tokens.

    :param text: str - input text
    :return: int - number of words
    """
    return len(text.split())

def get_letter_count(text):
    """
    Count the number of times each characters appears in the string

    String is converted to lowercase before.

    :param text: str - input text
    :return count_letters: dict lettter + count 
    """
    count_letters = {}
    text = text.lower()

    for letter in set(text):
        count_letters[letter] = text.count(letter)

    return count_letters

