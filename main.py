

def find_anagram(word, anagram):

    word = input('please enter a word: ')
    anagram = input('please enter a second word: ')

    str1 = "Knee"
    str2 = "keen"

if(len("str1") == len("str2")):

    #str1 = str1.lower()
    #str2 = str2.lower()

    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

if(len(str1) == len(str2)):

    
    sorted_str1 = sorted(word)
    sorted_str2 = sorted(anagram)

    if (sorted_str1 ==sorted_str2) :
        print('True')
    else:
        print('False')