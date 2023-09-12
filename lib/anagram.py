# your code goes here!



# Your class, Anagram should take a word on initialization; 
# instances should respond to a match() instance method that takes a list of possible anagrams. 
# It should return all matches in a list. If no matches exist, it should return an empty list.


class Anagram:
    def __init__(self, word):
        self.word = word
    

    def match(self, list):

        word_letters = [letter for letter in self.word]

        empty_list = []

        for each_word in list:
            list_word_letters = [letter for letter in each_word]
            if(sorted(word_letters) == sorted(list_word_letters)):
                empty_list.append(each_word)

        return empty_list






# initialize with a word inside of it 
# have a function named match
# match will take the word and also it will take a list
# take the word and split into letters
# for each listword in list
# separate each listword into letters
# sort the word 
# sort the listword
# see if they are equal
# if they are equal append it to an empty_list
# return the list


