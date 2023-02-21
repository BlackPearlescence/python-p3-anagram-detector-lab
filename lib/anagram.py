# your code goes here!

class Anagram:
    def __init__(self,word):
        self._word = word
    def match(self,word_list):
        myword = [*self._word]
        myword.sort()
        matches = []
        for i in range(len(word_list)):
            compword = [*word_list[i]]
            compword.sort()
            if(myword == compword):
                matches.append(word_list[i])
        return matches

ana = Anagram("enlist")
matches = ana.match(["listen", "silent", "hippopotamus"])
print(matches)