def LASTOFF(word_list):
    return [word[:-1] for word in word_list]

L = ['BOOKS', 'ARE', 'BEST']
N = LASTOFF(L)
print(N)
