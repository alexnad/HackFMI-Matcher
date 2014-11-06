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
    html += '  <tr>\n'
    html += '    <th>Mentors</th>\n'
    html += '    <th colspan="5">Teams</th>\n'
    html += '    <th colspan="100%">Teams on Queue</th>\n'
    html += '  </tr>\n'
    for mentor in list_of_mentors:
        html += '  <tr>\n'
        html += '    <th>{}</th>\n'.format(mentor)
        for team in mentor.teams:
            html += '    <td><p>{}</p><p>{}</p></td>\n'.format(team, team.room)
        html += '  </tr>\n'

    html += '</table>'
    file.write(html)
    file.close()

if __name__ == "__main__":
    main()

