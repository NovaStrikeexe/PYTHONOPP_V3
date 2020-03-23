
class Action:
    """
    Class action is responsible for the event that happened
    """

    def __init__(self, type_of_action: str):
        """

        :param type_of_action: Type of action
        :type type_of_action: str

        """
        self.type_of_action = type_of_action

    def set_Action(self, type_of_action):
        self.type_of_action = type_of_action

    def get_Action(self):
        """return self.type_of_action"""
        return self.type_of_action
