import requests
import re


def get_markdown():
    response = requests.get('https://raw.githubusercontent.com/Hackfmi/HackFMI-4/master/mentors.md')

    return response.text


def get_mentors():
    markdown = get_markdown()
    r = re.compile('### (.*?)\n')
    result = r.findall(markdown)
    return result
