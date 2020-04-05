from Classes import ShootingOfficer
from pony.orm import *
db = Database()

class ShotingRange(db.Entity):
    """
    Class ShootingRange class describing events that occur in the dash
    Also it includes ShootingOfficer

        :param sum_of_active_targets: Set sum of active targets
        :type sum_of_active_targets: int

        :param sum_of_all_targets: Set sum of all targets
         :type sum_of_all_targets:int

        :param type_of_shooting_range: Set type of shooting range
        :type type_of_shooting_range: bool

        :param officer:
        :watch in class ShootingOfficer.py
        """
    id_ShootingRange = PrimaryKey(int, auto=True)
    sum_of_active_targets = Required(int)
    sum_of_all_targets = Required(int)
    type_of_shooting_range = Required(bool)
    officer = Set(ShootingOfficer)