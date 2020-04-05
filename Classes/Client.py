from Classes import Human
from pony.orm import *


class Client(Human.Human):
    """

           :param name_of_human:
           :watch in class Human.py

           :param s_name_of_human:
           :watch in class Human.py

           :param age_of_human:
           :watch in class Human.py

           :param type_of_visit: Setting type of visit
           :type type_of_visit: bool
           """
    type_of_visit = Required(bool)
    """
    Client is a class a descendant of the class man,
    which will inherit a number of its fields and expand it with its own:
    property "visit" which takes the value 0 or 1
    """
