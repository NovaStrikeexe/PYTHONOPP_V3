from Classes import Client, ShootingOfficer, Cur_wepon, Action
"""
class OfficerClientWepon 
created to populate the list of events 
and participants of these events
"""

class OfficerClientWepon:
    def __init__(self,
                 client: Client,
                 officer: ShootingOfficer,
                 cur_wp: Cur_wepon,
                 action: Action):
        """
        :param client:Is an event participant
        :type client: object type client
        :watch in class Client.py

        :param officer:Is an event participant
        :type officer:object type officer
        :watch in class ShootingOfficer.py

        :param cur_wp:Is an event participant
        :type cur_wp: object type cur_wp
        :watch in class Cur_wepon.py

        :param action: Is an event that happened
        :type action: object type cur_wp
        :watch in class Action.py
        """
        self.client = client
        self.officer = officer
        self.cur_wp = cur_wp
        self.action = action

    def set_Client(self, client):
        self.client = client

    def set_Officer(self, officer):
        self.officer = officer

    def set_Cur_wp(self, cur_wp):
        self.cur_wp = cur_wp

    def set_Action(self, action):
        self.action = action

    def get_Client(self):
        return self.client

    def get_Officer(self):
        return self.officer

    def get_Cur_wp(self):
        return self.cur_wp

    def get_Action(self, action):
        return self.action
