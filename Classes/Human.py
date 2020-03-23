from pony.orm import *

db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)


class Human(db.Entity):
    id = PrimaryKey(int, auto=True)
    name_of_human = Required(str)
    s_name_of_human = Required(str)
    age_of_human = Required(int)

    """
    Class man is a progenitor class for all other people
    It has basic parameters for all other people:
    Name
    Second name
    Age
    """

    def __init__(self,
                 name_of_human: str,
                 s_name_of_human: str,
                 age_of_human: int):
        """

        :param name_of_human: Set Name of human
        :type name_of_human: str

        :param s_name_of_human: Set Second name of human
        :type s_name_of_human: str

        :param age_of_human: Set Age of human
        :type age_of_human: int

        """

        self.name_of_human = name_of_human
        self.s_name_of_human = s_name_of_human
        self.age_of_human = age_of_human
        """Setting parametars """

    def set_name_of_human(self, name_of_human):
        self.name_of_human = name_of_human

    def set_s_name_of_human(self, s_name_of_human):
        self.s_name_of_human = s_name_of_human

    def set_age_of_human(self, age_of_human):
        self.age_of_human = age_of_human

    def get_name_of_human(self):
        """:return self.name_of_human"""
        return self.name_of_human

    def get_s_name_of_human(self):
        """:return self.s_name_of_human"""
        return self.s_name_of_human

    def get_age_of_human(self):
        """:return self.age_of_human"""
        return self.age_of_human
