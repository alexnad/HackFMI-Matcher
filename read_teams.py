import csv
from team import Team
from datetime import datetime


class ReadTeams:
    CSV_FIELDS = 8
    CSV_FIRST_FIELD = 1

    def read_csv(self, file_name):
        csv_file = open(file_name, 'r')
        reader = csv.reader(csv_file, delimiter='|')

        teams = []

        for team in reader:
            name = self.__fix_whitespaces(team[0])

            room = self.__fix_whitespaces(team[self.CSV_FIELDS - 2])

            mentors = team[self.CSV_FIRST_FIELD:self.CSV_FIELDS - 2]
            mentors = self.__fix_list_whitespaces(mentors)

            time = self.__fix_whitespaces(team[self.CSV_FIELDS - 1])
            time = datetime.strptime(time, "%d/%m/%y %H:%M")

            teams.append(Team(name, mentors, time, room))

        csv_file.close()
        return teams

    def __fix_whitespaces(self, string):
        return string.strip()

    def __fix_list_whitespaces(self, mentors):
        fixed = []

        for string in mentors:
            fixed.append(self.__fix_whitespaces(string))

        return fixed
