class Mentor:
    def __init__(self, name):
        self.name = name
        self.teams = []

    def add_team(self, team_name):
        self.teams.append(team_name)

    def __repr__(self):
        return self.name
