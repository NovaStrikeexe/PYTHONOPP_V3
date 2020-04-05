from Classes.Database import *


class Human(db.Entity):
    id = PrimaryKey(int, auto=True)
    name_of_human = Required(str)
    s_name_of_human = Required(str)
    age_of_human = Required(int)
    """

         :param name_of_human: Set Name of human
         :type name_of_human: str

         :param s_name_of_human: Set Second name of human
         :type s_name_of_human: str
         :param age_of_human: Set Age of human
         :type age_of_human: int

         """

    """
    Class man is a progenitor class for all other people
    It has basic parameters for all other people:
    Name
    Second name
    Age
    """
