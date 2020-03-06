import sys
import os

# Load Anki library
sys.path.append("/usr/share/anki")
from anki.storage import Collection

# Define the path to the Anki SQLite collection
PROFILE_HOME = os.path.expanduser("~/.local/share/Anki2/Tests")
cpath = os.path.join(PROFILE_HOME, "collection.anki2")

# Load the Collection
col = Collection(cpath, log=True)  # Entry point to the API

# Use the available methods to list the notes
for cid in col.findNotes("tag:test"):
    note = col.getNote(cid)
    front = note.fields[0]  # "Front" is the first field of these cards
    print(front)

