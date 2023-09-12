def print_words(words):
    for word in words:
        print(word)
                    
def print_upper_words(words):
    for word in words: 
        print(wors.upper())

def print_e_words(words):
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word)

def print_specific_words(words, start_with):
    for word in words:
        for letter in start_with:
            if word.startswith(letter):
                print(word)
                break
