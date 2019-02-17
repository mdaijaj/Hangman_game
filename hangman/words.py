import string
import random

def load_words():
    Wordlist_filename="words.txt"
    print"Loading words list from file........."
    inFile=open(Wordlist_filename,'r')
    line=inFile.readline()
    word_list=string.split(line)
    print "The Total words is",len(word_list), "loaded.\n"
    return word_list

    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    word_list = ["navgurukul", "learning", "kindness"]
    return word_list

def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word