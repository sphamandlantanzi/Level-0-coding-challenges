word_1 = input().lower()
word_2 = input().lower()

def word_match(word_1,word_2):
    saver = []

    for i in range(len(word_1)):
        for j in range(len(word_2)):
            if word_1[i] == word_2[j]:
                saver.append(word_1[i])

    delete_repeat = set(saver)
    stick = ','.join(delete_repeat)

    ans = print("Common letters: " +stick)

    return ans

word_match(word_1,word_2)    
            

