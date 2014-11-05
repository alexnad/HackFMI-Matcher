import sys

from read_teams import ReadTeams
from get_mentors import get_mentors
from matcher import Matcher


def main():
    read = ReadTeams()
   # teams = read.read_csv(sys.argv[1])
    teams = read.read_csv('example.csv')
    list_of_mentors = get_mentors()
    matched_teams = Matcher(teams, list_of_mentors)
    return matched_teams.match_mentors()


if __name__ == "__main__":
    pass
