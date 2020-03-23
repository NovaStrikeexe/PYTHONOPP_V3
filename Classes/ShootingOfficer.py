from Classes import Human

"""
The ShootingOfficer  
Is the heir of the Human class
That extends it
With additional parameters
"""


class ShootingOfficer(Human.Human):
    def __init__(self,
                 name_of_human: str,
                 s_name_of_human: str,
                 age_of_human: int,
                 level_of_qualification: int,
                 work_experience: str,
                 work_schedule: str,
                 work_space: str):
        """

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

        :param work_space: Set work space
        :type work_space: str
        """
        Human.Human.__init__(self, name_of_human, s_name_of_human, age_of_human, level_of_qualification)
        self.work_experience = work_experience
        self.work_schedule = work_schedule
        self.work_space = work_space

    def set_work_experience(self, work_experience):
        self.work_experience = work_experience

    def set_work_schedule(self, work_schedule):
        self.work_schedule = work_schedule

    def set_work_space(self, work_space):
        self.work_space = work_space

    def get_work_experience(self):
        """:return self.work_experience"""
        return self.work_experience

    def get_work_schedule(self):
        """:return self.work_schedule"""
        return self.work_schedule

    def get_work_space(self):
        """:return self.work_space"""
        return self.work_space
