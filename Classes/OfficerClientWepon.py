from Classes import Client, ShootingOfficer, Cur_wepon, Action
from Classes.Database import *
"""
class OfficerClientWepon 
created to populate the list of events 
and participants of these events
"""

class OfficerClientWepon(db.Entity):
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
    id_OfficerClientWepon = PrimaryKey(int, auto=True)
    client = Set("Client")
    officer = Set("ShootingOfficer")
    cur_wp = Set("Cur_wepon")
    action = Set("Action")
