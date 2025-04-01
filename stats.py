def get_word_count(book_text):
    return len(book_text.split())

def get_char_count(book_text):
    char_counts = {}
    for c in book_text:
        char = c.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(dict):
    return dict["count"]

def get_sorted_char_count(char_counts):
    char_list = []
    for c in char_counts:
        char_list.append({"char": c, "count": char_counts[c]})
    char_list.sort(key=sort_on, reverse=True)
    return char_list