"""
### This module is about basic OOP
- Classes
- Constructor
- Encapsulated
- Inheritance
- Polymorphism
"""

from typing import Union

class Person(object): 
    
    def __init__(self, fname: str, lname: str, age: int):
        # Class Constructor
        """
            An example of simple class name Person that is a Super class

            Everything inheriting class, if overloading this method, must call it using super().

            Attributes:
            - first name
            - last name
            - age

            Methods
            - my_name
            - my_age 
        """
        # Attributes
        self.fisrt_name = fname
        self.last_name = lname
        self.age = age
    
    # method
    def my_name(self):
        """
            This method show your full name
        """
        print(f"My name is {self.fisrt_name} {self.last_name}")
    
    # method
    def my_age(self):
        """
            This method show your age
        """
        print(f"I'm {self.age} years old")
    

class Developer(Person):
    """
        This is an example of inheritance class from Super class (Person)

        use super() to get __init__ of super class attributes and methods
    """
    def __init__(self, fname: str, lname: str, age: int, language: Union[str, list]):
        """
            An example of class that inherit super class

            Attributes:
            - first name        
            - last name
            - age
            - language

            Methods:
            - my_name
            - my_language
            - my_github
        """
        super().__init__(fname, lname, age)
        self._language = language # Encasulate this attribute (protected)
    
    def my_name(self):
        """
            This method overriding my_method from super class

            that show your name with the same method as super class
        """
        super().my_name()
    
    def my_age(self):
        """
            This method overriding my_age from super class

            so you can change method but use the same method name
        """
        print(f"This method is Overriding from Super Class")
        print(f"My age is {self.age}")

    def my_languge(self):
        """
            This method show your computer language 
            
            that you use to develop programs
        """
        if isinstance(self.language, str):
            print(f"I use {self.language} to develop programs")

        elif isinstance(self.language, list):
            lang = ""
            for idx, val in enumerate(self.language):
                if idx == len(self.language) - 1:
                    lang += val
                else:
                    lang += f"{val}, "
            print(f"I use {lang} to develop programs")
    
    def my_github(self, name):
        """
            this method show developer github by input name parameter 
        """
        print(f"https://github.com/{name}")


if __name__ == "__main__":
    # Instantiate a class
    Mr_A = Person("John", "Wick", 24)
    Mr_A.my_name()
    
    # Instantiate sup class
    Mr_B = Developer(lname="Plypech", fname="Saharat" , age=24, language="Python") # change position of parameters
    Mr_B.my_name()
    Mr_B.my_age()
    Mr_B.my_languge()
    Mr_B.my_github("Saharatjj")