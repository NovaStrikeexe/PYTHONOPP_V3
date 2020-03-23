from NOVA_PYTHON_TEST.WEPONS_PY.Classes.ShootingOfficer import ShootingOfficer
from pony import orm
class ShotingRange:
    """
    Class ShootingRange class describing events that occur in the dash
    Also it includes ShootingOfficer
    """

    def __init__(self,
                 sum_of_active_targets: int,
                 sum_of_all_targets: int,
                 type_of_shooting_range: bool,
                 officer: ShootingOfficer):
        """

        :param sum_of_active_targets: Set sum of active targets
        :type sum_of_active_targets: int

        :param sum_of_all_targets: Set sum of all targets
         :type sum_of_all_targets:int

        :param type_of_shooting_range: Set type of shooting range
        :type type_of_shooting_range: bool

        :param officer:
        :watch in class ShootingOfficer.py
        """
        self.sum_of_active_targets = sum_of_active_targets
        self.sum_of_all_targets = sum_of_all_targets
        self.type_of_shooting_range = type_of_shooting_range
        self.officer = officer

    def set_sum_of_active_targets(self, sum_of_active_targets):
        self.sum_of_active_targets = sum_of_active_targets

    def set_sum_of_all_targets(self, sum_of_all_targets):
        self.sum_of_all_targets = sum_of_all_targets

    def set_type_of_shooting_range(self, type_of_shooting_range):
        self.type_of_shooting_range = type_of_shooting_range

    def set_officer(self, officer):
        self.officer = officer

    def get_sum_of_active_targets(self):
        """:return self.sum_of_active_targets"""
        return self.sum_of_active_targets

    def get_sum_of_all_targets(self):
        """:return self.sum_of_all_targets"""
        return self.sum_of_all_targets

    def get_type_of_shooting_range(self):
        """:return self.type_of_shooting_range"""
        return self.type_of_shooting_range

    def get_officer(self):
        """:return self.officer"""
        return self.officer
