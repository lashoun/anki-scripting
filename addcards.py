import sys
import os

# Load Anki library
sys.path.append("/usr/share/anki")
from anki.storage import Collection

# Define the path to the Anki SQLite collection
PROFILE_HOME = os.path.expanduser("~/.local/share/Anki2/Tests")

def bulk_loading_anki(deck, note_type, data_list, field_indices=[0, 1], tags=""):

    # Load the anki collection
    cpath = os.path.join(PROFILE_HOME, "collection.anki2")
    col = Collection(cpath, log=True)

    # Set the model
    modelBasic = col.models.byName(note_type)
    col.decks.current()['mid'] = modelBasic['id']

    # Get the deck
    deck = col.decks.byName(deck)

    # Iterate over idioms
    for data in data_list:

        # Instantiate the new note
        note = col.newNote()
        note.model()['did'] = deck['id']

        # Set the content
        for i, idx in enumerate(field_indices):
            note.fields[idx] = data[i]

        m = note.model()

        # Set the tags (and add the new ones to the deck configuration
        if len(tags) > 0:
            note.tags = col.tags.canonify(col.tags.split(tags))
            m['tags'] = note.tags

        col.models.save(m)

        # Add the note
        col.addNote(note)

    # Save the changes to DB
    col.save()
