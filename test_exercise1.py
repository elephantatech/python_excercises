import io
import unittest
import unittest.mock
from exercise1 import print_depth

class TestPrint_depth(unittest.TestCase):


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, x, expected_output, mock_stdout):
        print_depth(x)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_print_depth(self):
        a = {"key1": 1, "key2": {"key3": 1, "key4": {"key5": 4}}}
        self.assert_stdout(a, "key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\n")





