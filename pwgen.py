import random
import string
import os

dirname = os.path.dirname(__file__)
word_file = os.path.join(dirname, 'word-lists/words_alpha.txt')
WORDS = open(word_file).read().splitlines()
secure_random = random.SystemRandom()


def rand_word():
    return(secure_random.choice(WORDS).title())


def rand_punct():
    return(secure_random.choice(string.punctuation))


def gen_pw():
    password = "%s%s%s%s%s%s" % (
        rand_word(),
        rand_word(),
        rand_word(),
        random.randint(0, 9),
        random.randint(0, 9),
        rand_punct()
    )
    return(password)


for i in range(6):
    print(gen_pw())
