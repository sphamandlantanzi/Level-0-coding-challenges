

word = input().lower()

def vowel_hunter(word):
    saver = []
    vowels = ["a","e","i","o","u"]

    for i in range(len(vowels)):
        for j in range(len(word)):
            if vowels[i] == word[j]:
                saver.append(vowels[i])
    
    delete_repeat = set(saver)
    stick = ','.join(delete_repeat)

    ans = print("Vowels: " +stick)

    return ans

vowel_hunter(word)





