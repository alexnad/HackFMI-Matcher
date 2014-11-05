import sys

from read_teams import ReadTeams
from get_mentors import get_mentors
from matcher import Matcher


def main():
    read = ReadTeams()
    teams = read.read_csv(sys.argv[1])
    mentor_names = get_mentors()
    matched_teams = Matcher(teams, mentor_names)
    list_of_mentors = matched_teams.match_mentors()

    for mentor in list_of_mentors:
        mentor
        print('{}:'.format(mentor))
        for team in mentor.teams:
            print(team)
        print()

if __name__ == "__main__":
    main()
