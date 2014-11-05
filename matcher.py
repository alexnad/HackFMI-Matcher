from mentor import Mentor
from functools import cmp_to_key


class Matcher:

    def __init__(self, teams, mentor_names):
        self.teams = teams
        self.mentor_names = mentor_names
        self.current_mentor = None

    def match_mentors(self):
        mentors = []
        for name in self.mentor_names:
            self.current_mentor = Mentor(name)
            self.add_teams_to_mentor(self.current_mentor)
            mentors.append(self.current_mentor)

        return mentors

    def add_teams_to_mentor(self, mentor):
        teams = [team for team in self.teams if isinstance(team.get_choise(mentor.name), int)]
        sorted_teams = sorted(teams, key=cmp_to_key(self.__compare_teams))
        for team in sorted_teams:
            if not mentor.add_team(team):
                break

    def __compare_teams(self, team_1, team_2):
        team_1_choise = team_1.get_choise(self.current_mentor.name)
        team_1_application_time = team_1.application_time
        team_2_choise = team_1.get_choise(self.current_mentor.name)
        team_2_application_time = team_2.application_time

        if team_1_choise > team_2_choise:
            return 1

        if team_1_choise == team_2_choise:
            if team_1_application_time >= team_2_application_time:
                return 1

        return -1
