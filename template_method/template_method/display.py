from abc import ABCMeta, abstractclassmethod


class AbstractDisplay(metaclass=ABCMeta):
    @abstractclassmethod
    def print(self):
        pass 

    @abstractclassmethod
    def open(self):
        pass 

    @abstractclassmethod
    def close(self):
        pass 

    def display(self):
        self.open()
        for _ in range(5):
            self.print()
        self.close()


class CharDisplay(AbstractDisplay):
    def __init__(self, ch):
        self.__char = ch 

    def open(self):
        print('<<')
    
    def print(self):
        print(self.__char)
    
    def close(self):
        print(">>")


class StringDisplay(AbstractDisplay):
    def __init__(self, string):
        self.__string = string 
        self.__width = len(string)
    
    def open(self):
        self.__printLine()

    def print(self):
        print(f'|{self.__string}|')

    def close(self):
        self.__printLine()

    def __printLine(self):
        print('+')
        for _ in range(self.__width):
            print('-')
        print('+')