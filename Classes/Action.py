from pony.orm import *

db = Database()


class Action(db.Entity):
    """
    Class action is responsible for the event that happened
        :param type_of_action: Type of action
        :type type_of_action: str

    """
    id_action = PrimaryKey(int, auto=True)
    type_of_action = Required(str)
