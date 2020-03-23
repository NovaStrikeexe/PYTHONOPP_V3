from NOVA_PYTHON_TEST.WEPONS_PY.Classes import Human


class Client(Human.Human):
    """
    Client is a class a descendant of the class man,
    which will inherit a number of its fields and expand it with its own:
    property "visit" which takes the value 0 or 1
    """

    def __init__(self,
                 name_of_human: str,
                 s_name_of_human: str,
                 age_of_human: int,
                 level_of_qualification: int,
                 type_of_visit: bool
                 ):
        """

        :param name_of_human:
        :watch in class Human.py

        :param s_name_of_human:
        :watch in class Human.py

        :param age_of_human:
        :watch in class Human.py

        :param level_of_qualification
        :watch in class Human.py:

        :param type_of_visit: Setting type of visit
        :type type_of_visit: bool
        """
        Human.Human.__init__(self, name_of_human, s_name_of_human, age_of_human, level_of_qualification)
        """:
        :watch in class Human.py
        
        """
        self.type_of_visit = type_of_visit

    def set_type_of_visit(self, type_of_visit):
        self.type_of_visit = type_of_visit

    def get_type_of_visit(self):
        """:return self.type_of_visit"""
        return self.type_of_visit
