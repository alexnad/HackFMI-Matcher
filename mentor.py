class Mentor:
    TEAM_LIMIT = 5

    def __init__(self, name):
        self.name = name
        self.teams = []

    def add_team(self, team_name):
        if len(self.teams) < Mentor.TEAM_LIMIT:
            self.teams.append(team_name)
            return True
        return False

    def __repr__(self):
        return self.name

