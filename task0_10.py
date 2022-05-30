
word_1 = "House"
word_2 = "Computers"

def word_match(word_1,word_2):
    lower_word_1 = word_1.lower()
    lower_word_2 = word_2.lower()
    saver = []

    for i in range(len(lower_word_1)):
        for j in range(len(lower_word_2)):
            if lower_word_1[i] == lower_word_2[j]:
                saver.append(lower_word_1[i])

    delete_repeat = set(saver)
    stick = ','.join(delete_repeat)

    print("Common letters: " +stick)



word_match(word_1,word_2)    
            

