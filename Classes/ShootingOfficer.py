from Classes import Human
from Classes.Database import *
"""
The ShootingOfficer  
Is the heir of the Human class
That extends it
With additional parameters
"""


class ShootingOfficer(Human.Human):
    """
    The ShootingOfficer
    Is the heir of the Human class
    That extends it
    With additional parameters
        :param name_of_human:
        :watch in class Human.py

        :param s_name_of_human:
        :watch in class Human.py

        :param age_of_human:
        :watch in class Human.py

        :param level_of_qualification:
        :watch in class Human.py

        :param work_experience: Set work experience
        :type work_experience: str

        :param work_schedule: Set work schedule
        :type work_schedule: str
    """
    work_experience = Required(str)
    work_schedule = Required(str)
    OfficerClientWepon = Set("OfficerClientWepon")
    ShootingRange = Set("ShootingRange")
