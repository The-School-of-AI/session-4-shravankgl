import random
from decimal import *
import math

class Qualean:
    '''
    Qualean class that is inspired by Boolean+Quantum concepts. 
    We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1) 
    but it internally picks an imaginary state. The moment you assign it a real number, 
    it immediately finds an imaginary number random.uniform(-1, 1) and multiplies with it 
    and stores that number internally after using Bankers rounding to 10th decimal place
    '''
    def __init__(self, number = 1 ):
        '''
        Default value is 1
        '''
        if isinstance(number,str):
            raise ValueError ("String not supported")
        if number not in [-1, 0, 1]:
            raise ValueError ("Number not in [-1, 0, 1]")

        self.number = number        
        self.value = round(number*(random.uniform(-1,1)),10)
        #print(self.value)

    # defining object representation
    def __repr__(self):
        return f'Qualean Class Instance'

    # your other functions

    def __str__(self):
        return 'Qualean String for number: {0}'.format(self.number)

    def return_qualean(self):
        #return Decimal(self.value)
        return self.value

    def __sqrt__(self):
        #return math.sqrt(self.value)
        #return  Decimal(self.value).sqrt()
        if self.value >= 0:
            return round(Decimal(self.value).sqrt(), 10)
        else:
            #self.value = self.__invertsign__()
            return str(round(Decimal(self.__invertsign__()).sqrt(), 10)) + 'i'

    def __add__(self,other_object):
        if isinstance(other_object,str):
            raise TypeError ("Cannot add Qualean with String")
        if isinstance (other_object, Qualean):
            return self.value + other_object.value
        return self.value + other_object

    def __mul__(self,other_object):
        if isinstance(other_object,str):
            raise TypeError ("Cannot multiply Qualean with String")
        if isinstance (other_object, Qualean):
            return self.value * other_object.value
        return self.value * other_object

    def __eq__(self,other_object):
        if isinstance(other_object,str):
            raise TypeError ("Cannot compare Qualean with String")
        if isinstance (other_object, Qualean):
            return self.value == other_object.value
        return self.value == other_object

    def __float__(self):
        return float(self.value)

    def __ge__(self,other_object):
        if isinstance(other_object,str):
            raise TypeError ("Cannot compare Qualean with String")
        if isinstance (other_object, Qualean):
            return self.value >= other_object.value
        return self.value >= other_object

    def __gt__(self,other_object):
        if isinstance(other_object,str):
            raise TypeError ("Cannot compare Qualean with String")
        if isinstance (other_object, Qualean):
            return self.value > other_object.value
        return self.value > other_object

    def __invertsign__(self):
        return -self.value

    def __le__(self,other_object):
        if isinstance(other_object,str):
            raise TypeError ("Cannot compare Qualean with String")
        if isinstance (other_object, Qualean):
            return self.value <= other_object.value
        return self.value <= other_object

    def __lt__(self,other_object):
        if isinstance(other_object,str):
            raise TypeError ("Cannot compare Qualean with String")
        if isinstance (other_object, Qualean):
            return self.value < other_object.value
        return self.value < other_object

    def __bool__(self):
        return self.value != 0

    def get_item(self):
        return self.value

    def __and__(self,other_object):
        if not bool(self.value):
            return False
        else:
            if isinstance(other_object,Qualean) and other_object.value:
                return bool(self.value and other_object.value)
            else:
                return False

    def __or__(self,other_object):
        if None == other_object:
            return True
        if self.value:
            return True
        else:
            if isinstance(other_object,Qualean) and other_object.value:
                return bool(self.value or other_object.value)
            else:
                return False
