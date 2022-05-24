from unittest import TestCase
from unittest import main as testing

import finddashes as find_dashes

class TestReplaceDashFunction(TestCase):
    def test_replace_single_dash(self):
        s = find_dashes.replace_dash_at_index('Test string - for test purposes.', 12)
        self.assertEqual(s, 'Test string—for test purposes.')

class TestReplaceDashOnce(TestCase):
    def test_replace_once(self):
        s = find_dashes.replace_dashes_in_line('Test - string')
        self.assertEqual(s, 'Test—string')

class TestReplaceDashesHighlight(TestCase):
    def test_not_replace_dash_in_highlight(self):
        line = find_dashes.replace_dashes_in_line('*Test string - not to be changed*')
        self.assertEqual(line, '*Test string - not to be changed*')

    def test_replace_dash_to_the_right_to_highlight(self):
        line = find_dashes.replace_dashes_in_line('*Test string* this is - actually - to be changed')
        self.assertEqual(line, '*Test string* this is—actually—to be changed')

    def test_replace_dash_to_the_left_to_highlight(self):
        line = find_dashes.replace_dashes_in_line('this is - actually - to be changed *Test string*')
        self.assertEqual(line, 'this is—actually—to be changed *Test string*')

    def test_replace_dash_to_the_right_to_highlight_dash(self):
        line = find_dashes.replace_dashes_in_line('*Test - string* this is - actually - to be changed')
        self.assertEqual(line, '*Test - string* this is—actually—to be changed')

    def test_replace_dash_to_the_left_to_highlight_dash(self):
        line = find_dashes.replace_dashes_in_line('this is - actually - to be changed *Test - string*')
        self.assertEqual(line, 'this is—actually—to be changed *Test - string*')

class TestReplaceDashesLinks(TestCase):
    def test_not_replace_dash_in_links(self):
        line = find_dashes.replace_dashes_in_line('[Test string - not to be changed]()')
        self.assertEqual(line, '[Test string - not to be changed]()')

    def test_replace_dash_to_the_right_to_links(self):
        line = find_dashes.replace_dashes_in_line('[Test string - not to be changed]() this is - actually - to be changed')
        self.assertEqual(line, '[Test string - not to be changed]() this is—actually—to be changed')

    def test_replace_dash_to_the_left_to_links(self):
        line = find_dashes.replace_dashes_in_line('this is - actually - to be changed [Test string - not to be changed]()')
        self.assertEqual(line, 'this is—actually—to be changed [Test string - not to be changed]()')

class TestReplaceDashTables(TestCase):
    def test_skip_lines_in_tables(self):
        s = find_dashes.replace_dashes_in_line('| Test table string | to - actually - not be replaced |')
        self.assertEqual(s, '| Test table string | to - actually - not be replaced |')

if __name__ == '__main__':
    testing()
