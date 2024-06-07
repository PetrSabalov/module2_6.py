def single_root_words(root_word,*other_words):
    same_words = []
    for i in other_words:
        a = i.lower()
        if root_word.lower() in a:
            same_words.append(a)
        elif a in root_word.lower():
            same_words.append(i)
    return same_words
    print(same_words)

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))