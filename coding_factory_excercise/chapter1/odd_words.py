def odd_words_checker(words):
    """checks and returns the length of the words which have odd length"""
    odd_words = set(map(lambda word: len(word), filter(lambda word: len(word) % 2 != 0, words)))
    return odd_words

def main():
     words = ["apple", "banana", "cherry", "fig", "melon"] 
     odd_words = odd_words_checker(words)
     print(odd_words)
     print('-------')
     help(odd_words_checker)

if __name__ == '__main__':
    main() 