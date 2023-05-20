def five_letters_words_checker(words):
    """checks and returns the length of the words which have length more than five"""
    more_five_words = list(filter(lambda word: len(word) > 5, words))
    return more_five_words

def main():
     words = ["apple", "banana", "cherry", "fig", "melon"] 
     more_than_five_letter_words = five_letters_words_checker(words)
     print(more_than_five_letter_words)
     print('-------')
     help(five_letters_words_checker)

if __name__ == '__main__':
    main() 