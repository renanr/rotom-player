import requests
from bs4 import BeautifulSoup

response = requests.get("http://replay.pokemonshowdown.com/gen7randombattle-595337782")
content = response.content
parser = BeautifulSoup(content, 'html.parser')
body = parser.body

lines = []
for line in body.script.text.split("\n"):
    lines.append(line.split("|")[1:])
nb_lines = len(lines)

turns = []
turn_names = [] # first line of turn_names corresponds to second line of turns
i = 0
while(i < nb_lines):
    turn = []
    while(lines[i][0] != 'turn'):
        turn.append(lines[i])
        i += 1
    turns.append(turn)
    turn_names.append(lines[i])
    i += 1