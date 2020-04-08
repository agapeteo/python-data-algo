import unittest
from .reverse import reverse


class Test(unittest.TestCase):
    def testReverse(self):
        self.assertEqual(reverse('hi'), 'ih')
        self.assertEqual(reverse('hola'), 'aloh')
        self.assertEqual(reverse('bla'), 'alb')


if __name__ == '__main__':
    unittest.main()
