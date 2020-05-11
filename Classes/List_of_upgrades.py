from Classes.Database import *

class List_of_upgrades(db.Entity):
    """Class List_of_upgrages is responsible for the list of modifications for each weapon
     He takes data on possible modifications from the database, which will be connected to the project
        :param scope: This parameter is responsible for the scope that can be installed.
        :type scope: str
        :param handle: This parameter is responsible for the handle that can be installed.
        :type handle: str
        :param mag: This parameter is responsible for the сlip that can be installed.
        :type int
        :param type_of_mag:This parameter is responsible for the type of mag that can be used.
        :type of mag: str
        :param type_of_bulets:This parameter is responsible for the type of bulets that can be used.
        :type type_of_bulets: str

    """
    scope = Required(str)
    handle = Required(str)
    mag = Required(int)
    type_of_mag = Required(str)
    type_of_bulets = Required(str)
    cur_wepons = Set("Cur_wepon")