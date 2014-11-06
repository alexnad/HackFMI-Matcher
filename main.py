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

    file = open('mentors.html', 'w')
    html = ''
    html += '<table border="1">\n'
    for mentor in list_of_mentors:
        html += '  <tr>\n'
        html += '    <th>{}</th>\n'.format(mentor)
        for team in mentor.teams:
            html += '    <td>{}</td>\n'.format(team)
        html += '  </tr>\n'

    html += '</table>'
    file.write(html)

if __name__ == "__main__":
    main()

