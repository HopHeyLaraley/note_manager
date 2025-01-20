import unittest
from interface import ReadNote, SearchNote
from data import *
from models import Note
from utils import validate_date
from datetime import datetime

class TestNotExistNotes(unittest.TestCase):
    def test_show_not_exist_notes(self):
        print('Test 1')
        self.assertEqual(type(ReadNote().read_all()), type(1))

class TestexistNotes(unittest.TestCase):
    def test_show_exist_notes(self):
        from data import load_notes
        load_notes('../data/notes.json')
        print('Test 2')
        self.assertEqual(type(ReadNote().read_all()), type(dict()))

class TestFindNote(unittest.TestCase):
    def test_search_by_status(self):
        self.assertEqual(SearchNote().search_by_status('Несуществующий статус'), {})

class TestFileMemory(unittest.TestCase):
    def test_load_notes(self):
        self.assertEqual(load_notes('../data/notes.json'), 1)

    def test_save_notes(self):
        self.assertEqual(save_notes('../data/notes.json'), 1)

    def test_load_statuses(self):
        self.assertEqual(load_statuses('../data/statuses.json'), 1)

    def test_save_statuses(self):
        self.assertEqual(save_statuses('../data/statuses.json'), 1)

    def test_delete_none_from_dict(self):
        self.assertEqual(delete_from_dict({1: Note()}), 0)

class TestValidate(unittest.TestCase):
    def test_validate_incorrect_date1(self):
        self.assertEqual(validate_date('01.01.2000'), 0)

    def test_validate_incorrect_date2(self):
        self.assertEqual(validate_date('2000-01-20'), 0)

    def test_validate_incorrect_date3(self):
        self.assertEqual(validate_date('01/01/2000'), 0)

    def test_validate_correct_date(self):
        self.assertEqual(validate_date('01-01-2000'), datetime.strptime('01-01-2000', '%d-%m-%Y'))


if __name__ == "__main__":
    unittest.main()