import unittest
from db import *
from models import Note
from interface import CreateNote
from utils import date_format


test_db_path = '../db/notes.db'

class TestBD(unittest.TestCase):
    def test_database(self):
        test_data = CreateNote().input_note_data()
        test_note = Note(test_data)
        save_note_to_db(test_note, test_db_path)

        read_notes = load_notes_from_db(db_file_path=test_db_path)
        last_id = max([i for i, n in read_notes.items()])
        last_note = read_notes[last_id]

        res = test_data['username'] == last_note['username']
        res = res and test_data['titles'] == last_note['titles']
        res = res and test_data['content'] == last_note['content']
        res = res and test_data['status'] == last_note['status']
        res = res and date_format(test_data['issue_date']) == date_format(last_note['issue_date'])

        if res:
            print('Notes similary')

if __name__ == "__main__":
    unittest.main()
