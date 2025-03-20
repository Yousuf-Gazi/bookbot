def get_number_of_words(contents):
    word_list = contents.split()
    return len(word_list)

def count_char(contents):
    char_dict = {}
    for char in contents.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def sort_counted_char(char_dict):
    # labeled_dict = [{"char": key, "count": value} for key, value in char_dict.items()]
    labeled_dict = []
    for char in char_dict:
        labeled_dict.append({"char": char, "count": char_dict[char]})

    labeled_dict.sort(reverse=True, key=sort_on)
    return labeled_dict