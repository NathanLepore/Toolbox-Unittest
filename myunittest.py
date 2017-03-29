import unittest


def listsort():

    list_nums = [-5, -3, -5, -2, -1, 0, 2, 1, 3, 5, 4]
    list_nums = [i for i in list_nums if i >= 0]
    return sorted(list_nums)


class TestStringMethods(unittest.TestCase):

    def test_listsort(self):
        self.assertEqual(listsort(), [0, 1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
