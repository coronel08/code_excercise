"""
https://www.python-course.eu/python3_multiple_inheritance.php
An example of building multi inheritance/ diamond. A new class with Multiple Inheritance
ClockAndCalendar inherits from both Clock and Calendar. 
"""
# https://www.geeksforgeeks.org/oop-in-python-set-3-inheritance-examples-of-object-issubclass-and-super/




# https://www.datacamp.com/community/tutorials/super-multiple-inheritance-diamond-problem
class Tokenizer:
    def __init__(self,text):
        print("Start Tokenizer")
        self.tokens = text.split()
        print("End Tokenizer")
    

class WordCounter(Tokenizer):
    """Count words in text"""
    def __init__(self,text):
        print("Start WordCounter")
        super().__init__(text)
        self.word_count = len(self.tokens)
        print("End WordCounter")


class Vocabulary(Tokenizer):
    """Find unique words in text"""
    def __init__(self,text):
        print("Start Vocabulary")
        super().__init__(text)
        self.vocab = set(self.tokens)
        print("End Vocabulary")


class TextDescriber(WordCounter,Vocabulary):
    """Describe text with multiple metrics"""
    def __init__(self, text):
        print("Start TextDescriber")
        super().__init__(text)
        print("End TextDescriber")


test = TextDescriber("Smoking on that loud loud")
print("--------")
print(test.tokens)
print(test.vocab)
print(test.word_count)



"""
Multiple Inheritance example, calls getMiles(self) and getMiles(base) -------------------------------------
https://www.geeksforgeeks.org/python-super/
"""
class Animal:
    def __init__(self):
        self.legs = 4
        self.domestic = True
        self.tail = True
        self.mammals = True
    
    def isMammal(self):
        if self.mammals:
            print("It is a mammal")    

    def getMiles(self):
        return 2

class Dogs(Animal):
    def __init__(self):
        super().__init__()
    
    def isMammal(self):
        super().isMammal()
    
    def getMiles(self):
        return 1

    # doesnt need init above to access self and super of same name
    def printFactors(self):
        print(f"{self.getMiles()} and {super().getMiles()} ")

class Horses(Animal):
    def __init__(self):
        super().__init__()
    
    def hasTailandLegs(self):
        if self.tail and self.legs == 4:
            print("Has legs and tail")

cooky = Dogs()
cooky.isMammal()
cooky.printFactors()
