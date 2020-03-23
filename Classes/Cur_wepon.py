from NOVA_PYTHON_TEST.WEPONS_PY.Classes import List_of_upgrades, Wepons


class Cur_wepon(Wepons.Wepons):
    """
The Cur_wepon class is responsible for the weapon issued.
It is an inheritor of the Wepons class and includes the List_of_upgrades class.
It has an additional field in_action which shows the state of the object at the moment
    """

    def __init__(self,
                 mark_of_wepon: str,
                 company_constrator: str,
                 level_of_access: int,
                 ammo: int,
                 calibr: float,
                 list_of_upgrades: List_of_upgrades):
        """

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
        Wepons.Wepons.__init__(self, mark_of_wepon, company_constrator, level_of_access, ammo, calibr)
        self.list_of_upgrades = list_of_upgrades

    def set_list_of_upgrades(self, list_of_upgrades):
        self.list_of_upgrages = list_of_upgrades

    def get_list_of_upgrades(self):
        """:return self.list_of_upgrages"""
        return self.list_of_upgrages
