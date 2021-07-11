"""
For a list containing strings,
check which characters exist,
then replace that character with a random character.
"""
# ................................................................ Imports
from random import *
# ................................................................ Main Function
def make_words(words=["tiger", "airplane", "cocaine"]):
    return words

def replace_character():

    string = make_words()
    string = choice(string)
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    new_words = []
    letters_in_word = []
    letters_not_in_word = []
    
    for a in alphabet:
        if a not in string:
            # print("'{}'\t NOT IN\t'{}'".format(a, string))
            letters_not_in_word.append(a)
        elif a in string:
            # print("'{}'\tEXISTS IN\t'{}'".format(a, string))
            letters_in_word.append(a)
    print()
    print("these letters are in '{}'\n{}".format(string, ", ".join(letters_in_word)))
    print()
    print("these letters are not in '{}'\n{}".format(string, ", ".join(letters_not_in_word)))

    count = 0

    for i in range(len(alphabet)):
        count += 1
        rand_alpha = choice(alphabet)
        replace_char = alphabet[i]
            
        if rand_alpha in string:     
            print()
            print('character {} exists in {}'.format(rand_alpha, string))
            print('replacing "{}" in {} with "{}"'.format(rand_alpha, string, replace_char))
            print('printing new word..')
            print()

            new_string = string.replace(rand_alpha,replace_char)
            new_words.append(new_string)

            print(new_string)

    new_words = ", ".join(new_words)
    return new_words
# ................................................................ On Run, Export/Import
if __name__ == "__main__":
    make_words()
    replace_character()
# ................................................................ Updates
# ................................................................ Bugs
