def vowel_hunter(word):
    lower_word = word.lower()
    lister = []
    vowels = ["a","e","i","o","u"]

    for i in range(len(vowels)):
        for j in range(len(lower_word)):
            if vowels[i] == lower_word[j]:
                lister.append(vowels[i])
    
    delete_repeat = set(lister)
    stick = ', '.join(delete_repeat)

    print("Vowels: " +stick)

vowel_hunter("Umuzi")





