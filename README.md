HackFMI-Matcher
===============

Program that matches teams with mentors (for HackFMI).

### Dependencies:
><a href="http://docs.python-requests.org/en/latest/user/install/#install">requests</a>

### Getting Started:
>Run <b>main.py</b> passing <b>*.csv</b> file from the console
>
>csv should be formated like:
>
><b>Team , Room , Mentor1 , Mentor2 , Mentor3 , Mentor4 , Mentor5 , DD/MM/YY HH:MM</b>
>
>The program will generate file <b>mentors.html</b> containing html table
>with the Mentors as first column and the teams they will gide as next five columns.
>(Teams that have picked a certen mentor, but were not from the first five, are left on queue wich is also generated
>in the html.)

The list with mentors is automaticly generated from <a href="https://github.com/Hackfmi/HackFMI-4/blob/master/mentors.md">here</a>
