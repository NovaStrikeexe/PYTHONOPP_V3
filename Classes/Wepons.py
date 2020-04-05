from Classes.Database import *


class Wepons(db.Entity):
    """
    Weapon class is responsible for creating weapons class objects

        :param mark_of_wepon: Set Mark of wepon
         :type mark_of_wepon: str

        :param company_constrator: Set Company constrator
        :type company_constrator: str

        :param ammo: Set quantity of ammo
        :type ammo: int

        :param calibr: Set type of  calibr
        :type calibr: float
        """
    """Setting parameters """
    id_wepon = PrimaryKey(int, auto=True)
    mark_of_wepon = Required(str)
    company_constrator = Required(str)
    ammo = Required(int)
    calibr = Required(float)
