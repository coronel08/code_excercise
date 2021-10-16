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





"""
Decorators @property https://www.freecodecamp.org/news/python-property-decorator/
Exmaple used https://blog.teclado.com/python-abc-abstract-base-classes/
"""

from abc import ABC, abstractmethod

class Animal(ABC): # Inherit from ABC
    @property
    def food_eaten(self):
        return self._food
    
    @food_eaten.setter
    def food_eaten(self, food):
        if food in self.diet:
            self._food = food
        else:
            raise ValueError(f"You can't feed this animal with {food}")

    @property
    @abstractmethod
    def diet(self):
        pass

    @abstractmethod # Decorator to define abstract method
    def feed(self, action):
        pass

class Lion(Animal):
    @property
    def diet(self):
        return ["antelope", "cheetah", "buffalo"]

    def feed(self, time):
        print(f"Feeding a lion {self._food} at {time}")

class Panda(Animal):
    @property
    def diet(self):
        return ["bamboo", "grass"]

    def feed(self, time):
        print(f"Feeding a panda {self._food} at {time}")

class Snake(Animal):
    @property
    def diet(self):
        return ["frog", "rabbit"]

    def feed(self, time):
        print(f"Feeding a snake {self._food} at {time}")


leo =Lion()
leo.food_eaten="antelope"
leo.feed("10pm")

adam = Snake()
adam.food_eaten = "frog"
adam.feed("8pm")
