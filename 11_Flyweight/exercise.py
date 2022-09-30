"""Flyweight pattern task

Given a Sentence class whose constructor takes a string (such as "hello world").

You need to implement the API in such a way that the indexer returns a flyweight through which you can translate
specific words from the string to uppercase. Here is an example of using such an API:

sentence = Sentence('hello world')
sentence[1].capitalize = True
print(sentence) # writes 'hello WORLD'"""


"""
# *Start template
class Sentence:
    def __init__(self, plain_text):
        pass
        # ToDo
"""


# ?Solution
class Sentence:
    def __init__(self, plain_text):
        self.words = plain_text.split(" ")
        self.tokens = {}

    def __getitem__(self, item):
        wt = self.WordToken()
        self.tokens[item] = wt

        return self.tokens[item]

    class WordToken:
        def __init__(self, capitalize=False):
            self.capitalize = capitalize

    def __str__(self):
        result = []

        for i in range(len(self.words)):
            w = self.words[i]

            if i in self.tokens and self.tokens[i].capitalize:
                w = w.upper()

            result.append(w)

        return " ".join(result)


sentence = Sentence("Hello world! I'm software engineer :D")
print(sentence)

sentence[1].capitalize = True
sentence[3].capitalize = True
print(sentence)
