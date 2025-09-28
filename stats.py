def get_num_words(text):
    return len(text.split())

def num_of_chars(text):
    chars = {}
    lowered = text.lower()
    for char in lowered:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def sort_on(item):
    return item["num"]

def get_sorted_list(chars):
    sorted_list = []
    for char, num in chars.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": num})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list
    