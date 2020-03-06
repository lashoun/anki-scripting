import sys
import os
import addcards

# Load Anki library
sys.path.append("/usr/share/anki")
from anki.storage import Collection

# Define the path to the Anki SQLite collection
PROFILE_HOME = os.path.expanduser("~/.local/share/Anki2/Tests")

words = []
definitions = []
natures = []
with open("dico/words.txt") as fin:
    for line in fin:
        words.append(line[:-1])  # [:-1] to remove "\n"
with open("dico/natures.txt") as fin:
    for line in fin:
        natures.append(line[:-1])
with open("dico/definitions2.txt") as fin:
    for line in fin:
        definitions.append(line[:-1])
data = []
for i in range(len(words)):
    data.append([words[i], definitions[i], natures[i]])

addcards.bulk_loading_anki("Français", "Fr (and reversed card)", data, field_indices=[0, 1, 3], tags="")
