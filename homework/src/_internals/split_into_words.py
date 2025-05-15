def split_into_words(lines):
    # pass
    words = []
    for line in lines:
        words.extend(word.strip(",.!?") for word in line.split())
    return words
