class List_of_upgrades:
    """Class List_of_upgrages is responsible for the list of modifications for each weapon
     He takes data on possible modifications from the database, which will be connected to the project"""

    def __init__(self,
                 scope: str,
                 handle: str,
                 mag: int,
                 type_of_mag: str,
                 type_of_bulets: str):
        """
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
        self.scope = scope
        self.handle = handle
        self.mag = mag
        self.type_of_mag = type_of_mag
        self.type_of_bulets = type_of_bulets

    def set_scope(self, scope):
        self.scope = scope

    def set_handle(self, handle):
        self.handle = handle

    def set_mag(self, mag):
        self.mag = mag

    def set_type_of_mag(self, type_of_mag):
        self.type_of_mag = type_of_mag

    def set_type_of_bulets(self, type_of_bulets):
        self.type_of_bulets = type_of_bulets

    def get_scope(self):
        """:return self.scope"""
        return self.scope

    def get_handle(self):
        """:return self.handle"""
        return self.handle

    def get_mag(self):
        """:return self.mag"""
        return self.mag

    def get_type_of_mag(self):
        """:return self.type_of_mag"""
        return self.type_of_mag

    def get_type_of_bulets(self):
        """:return self.type_of_bulets"""
        return self.type_of_bulets
