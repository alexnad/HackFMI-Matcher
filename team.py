class Team:
    def __init__(self, name, mentors, application_time):
        self.name = name
        self.mentors = mentors
        self.application_time = application_time

    def get_choise(self, mentor):
        if mentor in self.mentors:
            return self.mentors.index(mentor)
        return False
