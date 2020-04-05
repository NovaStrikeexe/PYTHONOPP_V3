from Classes import List_of_upgrades, Wepons
from Classes.Database import *


class Cur_wepon(Wepons.Wepons):
    """
The Cur_wepon class is responsible for the weapon issued.
It is an inheritor of the Wepons class and includes the List_of_upgrades class.
It has an additional field in_action which shows the state of the object at the moment

        :param mark_of_wepon:
        :watch in class Wepons.py

        :param company_constrator:
        :watch in class Wepons.py

        :param level_of_access:
        :watch in class Wepons.py

        :param ammo:
        :watch in class Wepons.py

        :param calibr:
        :watch in class Wepons.py

        :param list_of_upgrades:
        :watch in class List_of_upgrades.py
    """
    list_of_upgrades = Set(List_of_upgrades)
