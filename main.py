#main.py
#
#Author:        Farjad Tariq
#Version:       2023/08/23
#
#Purpose:       The purpose of this is to write a Python program 
#               that creates all the sequences of four English letters 
#               and determines the sequences that are English language 4 letter words.

from time import ctime

def getWords(filename):
    '''Given the name of a file containing one word to a
    line return a list of words from the file.'''
    #wordlist - the name of the file containing the words
    #infile - a reference to the file to be read
    #words - the words from the file as one big string
    infile = open(filename, 'r')
    words = infile.read()
    infile.close()
    return words.splitlines()

def fourLetterSequences(words):
    '''Creates a list of all possible four letter sequences from the alphabet
        and checks to see if they are in the english language and then
        creates a list of those words. Counts the total sequences and the words.'''
    #sequences = the total number of possible four letter sequences
    #word = a single string of four letters 
    #newWords = a list of words from the sequences that are in the english language
    #count = total number of words in newWords
    #letter = alphabets of the english language
    sequences = 0
    count = 0
    newWords = []
    letters = "abcdefghijklmnopqrstuvwxyz"

    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                for letter4 in letters:
                    word = (letter1+letter2+letter3+letter4)
                    sequences += 1      

                    if word in words:
                        newWords.append(word)
                        count += 1
    return newWords, sequences, count

def displayfourLetterWords(words, sequences):
    '''Prints/Displays the number of sequences and words returned from
        fourLetterSequences. Also prints the first 10 and the last 10
        words in the list newWords.'''
    #words = newWords(list of words created out of the four letter sequences)
    #sequences = the total number of possible four letter sequences
    #count = total number of words in newWords
    words, sequences, count = fourLetterSequences(words)
    print("\nOf the %i sequences of four letter words there are %i words." %  (sequences, count))
    print("\nThe first 10 four letter words are:\n",words[0:10])
    print("\nThe last 10 four letter words are:\n",words[-10:])

def main():
    '''The main program, combines all the functions together. Inputs the name
        of file that contains the four letter words from the english language
        and gives the number of words in it.'''
    #filename = name of file containing the four letter english language words
    #words = newWords(list of words created out of the four letter sequences)
    #sequences = the total number of possible four letter sequences
    #count = total number of words in newWords
    print("\n" + "-" * 80)
    filename = input("Enter the name of the file containing the words: ")

    #calls list of english language words
    words = getWords(filename)
    #calls our list of english language words, our total number of
    # four letter sequences and the number of words in the sequences
    newWords, sequences, count = fourLetterSequences(words)

    print("\nThere are %i four letter words in the file." % (count))
    #calls the function which prints all the lists and counts
    displayfourLetterWords(words, sequences)

def displayTerminationMessage():
    print("""
Programmed by Farjad Tariq
Date: %s
End of processing.\n""" % ctime())

main()
displayTerminationMessage()