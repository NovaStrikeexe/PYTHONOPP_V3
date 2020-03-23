class Wepons:
    """
    Weapon class is responsible for creating weapons class objects
    """
    def __init__(self,
                 mark_of_wepon: str,
                 company_constrator: str,
                 level_of_access: int,
                 ammo: int,
                 calibr: float):
        """

        :param mark_of_wepon: Set Mark of wepon
         :type mark_of_wepon: str

        :param company_constrator: Set Company constrator
        :type company_constrator: str

        :param level_of_access: Set Level of access
        :type level_of_access: int

        :param ammo: Set quantity of ammo
        :type ammo: int

        :param calibr: Set type of  calibr
        :type calibr: float
        """
        self.mark_of_wepon = mark_of_wepon
        self.company_constrator = company_constrator
        self.level_of_access = level_of_access
        self.ammo = ammo
        self.calibr = calibr

    """Setting parameters """

    def set_mark_of_wepon(self, mark_of_wepon):
        self.mark_of_wepon = mark_of_wepon

    def set_company_constrator(self, company_constrator):
        self.company_constrator = company_constrator

    def set_level_of_access(self, level_of_access):
        self.level_of_access = level_of_access

    def set_ammo(self, ammo):
        self.ammo = ammo

    def set_calibr(self, calibr):
        self.calibr = calibr

    def get_mark_of_wepon(self):
        """:return self.mark_of_wepon"""
        return self.mark_of_wepon

    def get_company_constrator(self):
        """:return self.company_constrator"""
        return self.company_constrator

    def get_level_of_access(self):
        """:return self.level_of_access"""
        return self.level_of_access

    def get_ammo(self):
        """:return self.ammo"""
        return self.ammo

    def get_calibr(self):
        """:return self.calibr"""
        return self.calibr
